import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

import docker
import yaml
from docker.errors import ContainerError
from yaml.loader import SafeLoader

from .const import BST_PATH, CONF_NAME


class JobException(Exception):
    pass


@dataclass
class Job:
    app_path: Path
    image: str
    run_cmd: str
    build_cmd: str = ""
    install_requires: str = ""
    name: str = ""
    description: str = ""
    version: str = ""
    container_name: str | None = None
    datasets_path: Path = Path("datasets")
    language: str | None = None

    def __post_init__(self):
        self.language = self.language or self.app_path.name
        self.container_name = (
            self.container_name
            or f"{self.name or self.language}-{str(uuid.uuid4())[:8]}"
        )

    @property
    def app_path_str(self) -> str:
        return str(self.app_path.resolve())

    @property
    def datasets_path_str(self) -> str:
        return str(self.datasets_path.resolve())

    @staticmethod
    def FROM_YAML(path_to_folder: Path, conf_name: str = CONF_NAME) -> "Job":
        conf = None
        with open(path_to_folder / conf_name) as f:
            conf = yaml.load(f, SafeLoader)
        if not conf:
            raise JobException()
        job = Job(
            app_path=path_to_folder,
            image=conf["image_name"],
            run_cmd=conf["run_command"],
            build_cmd=conf.get("build_command", ""),
            install_requires=conf.get("install_requires", ""),
            name=conf.get("name", ""),
            description=conf.get("description", ""),
            version=conf.get("version", ""),
        )
        return job

    def _get_command(self, amount: int = 10000000) -> str:
        command = [
            "cp -r app/* .",
            self.install_requires or "echo",
            self.build_cmd or "echo",
            f"{self.run_cmd} {amount}",
        ]
        return " && ".join(command)

    def run(self, amount: int = 10000000):
        client = docker.from_env()

        volumes = {
            self.app_path_str: {"bind": "/app", "mode": "ro"},
            self.datasets_path_str: {"bind": "/datasets", "mode": "ro"},
        }
        output_str = ""
        try:
            output = client.containers.run(
                image=self.image,
                name=self.container_name,
                remove=True,
                volumes=volumes,
                command=f'bash -c "{self._get_command(amount)}"',
                stdout=True,
                stderr=True,
                stdin_open=True,
            )
            output_str = output.decode()
        except ContainerError as e:
            output_str += str(e)
        return output_str

    def to_dict(self) -> dict[str, str]:
        dictionary = asdict(self)
        del dictionary["app_path"]
        del dictionary["datasets_path"]
        del dictionary["container_name"]
        return dictionary


def get_jobs(bst_path: Path = BST_PATH) -> List[Job]:
    bst_list = [x for x in bst_path.iterdir() if x.is_dir()]
    jobs: List[Job] = []
    for bst in bst_list:
        jobs.append(Job.FROM_YAML(bst))
    return jobs

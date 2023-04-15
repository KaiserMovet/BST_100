import uuid
from dataclasses import dataclass
from pathlib import Path

import docker
import yaml
from docker.errors import ContainerError
from docker.types import LogConfig
from yaml.loader import SafeLoader


@dataclass
class Runner:
    image_name: str
    app_path: Path
    run_command: str
    container_name: str | None = None
    build_command: str = ""
    datasets_path: Path = Path("datasets")

    def __post_init__(self):
        self.container_name = self.container_name or str(uuid.uuid4())[:8]

    @staticmethod
    def FROM_FOLDER(language_name: str):
        app_path = Path("BST/") / language_name
        with open(app_path / "conf.yaml") as f:
            conf = yaml.load(f, SafeLoader)
        return Runner(
            image_name=conf["image_name"],
            app_path=app_path,
            run_command=conf["run_command"],
            build_command=conf.get("build_command", ""),
        )

    @property
    def app_path_str(self) -> str:
        return str(self.app_path.resolve())

    @property
    def datasets_path_str(self) -> str:
        return str(self.datasets_path.resolve())

    @staticmethod
    def _wsl_path(path: Path) -> str:
        # Convert Path object to string
        path = path.resolve()
        path_str = str(path)

        # Replace backslashes with slashes
        path_str = path_str.replace("\\", "/")

        # Convert drive letter to lowercase
        drive_letter = path_str[0].lower()

        # Replace "C:/" with "/mnt/c/"
        path_str = path_str.replace(
            drive_letter + ":/", "/mnt/" + drive_letter + "/"
        )

        return path_str

    def _get_command(self, amount: int = 10000000) -> str:
        command = [
            "cp -r app/* .",
            self.build_command or "echo",
            f"{self.run_command} {amount}",
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
                image=self.image_name,
                name=self.container_name,
                remove=False,
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

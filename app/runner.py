import uuid
from dataclasses import dataclass
from pathlib import Path

import docker
from docker.types import LogConfig


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

    @property
    def app_path_str(self) -> str:
        return self._wsl_path(self.app_path)

    @property
    def datasets_path_str(self) -> str:
        return self._wsl_path(self.datasets_path)

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
            "cp app/* .",
            "ls",
            self.build_command,
            f"{self.run_command} {amount}",
        ]
        return " && ".join(command)

    def run(self, amount: int = 10000000):
        client = docker.from_env()

        volumes = {
            self.app_path_str: {"bind": "/app", "mode": "ro"},
            self.datasets_path_str: {"bind": "/datasets", "mode": "ro"},
        }

        lc = LogConfig(
            type=LogConfig.types.JSON,
            config={"max-size": "1g", "labels": "production_status,geo"},
        )

        output = client.containers.run(
            image=self.image_name,
            name=self.container_name,
            auto_remove=False,
            volumes=volumes,
            command=f'bash -c "{self._get_command(amount)}"',
            stdout=True,
            stderr=True,
        )
        output_str = output.decode()
        del client
        return output_str

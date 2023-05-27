from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml
from jinja2 import Environment, FileSystemLoader, Template
from requests import get
from yaml.loader import SafeLoader


@dataclass
class Job:
    language: str
    image: str
    run_cmd: str
    build_cmd: str = ""


def get_env() -> Environment:
    return Environment(loader=FileSystemLoader("templates/"))


def get_template(name: str) -> Template:
    env = get_env()
    template = env.get_template(name)
    return template


def get_jobs(bst_path: Path) -> list[Job]:
    bst_list = [x for x in bst_path.iterdir() if x.is_dir()]
    jobs: List[Job] = []
    for bst in bst_list:
        print(bst)
        conf = None
        with open(bst / "conf.yaml") as f:
            conf = yaml.load(f, SafeLoader)
        print(conf)
        job = Job(
            language=bst.name,
            image=conf["image_name"],
            run_cmd=conf["run_command"],
            build_cmd=conf.get("build_command", ""),
        )
        jobs.append(job)
    return jobs


def get_bst_path() -> Path:
    return Path("BST/")


def main():
    bst_path = get_bst_path()
    jobs = get_jobs(bst_path)
    languages = [job.language for job in jobs]
    amount = str(
        [
            100,
            1_000,
            10_000,
            100_000,
            1_000_000,
            2_000_000,
            3_000_000,
            4_000_000,
            5_000_000,
            6_000_000,
            7_000_000,
            8_000_000,
            9_000_000,
            10_000_000,
        ]
    )
    attempts = str(list(range(1, 4)))

    # BST jobs
    template_bst = get_template("main.yaml.j2")

    rendered_template_bst = template_bst.render(
        jobs=jobs, amount=amount, attempts=attempts, languages=languages
    )
    with open("./.github/workflows/main.yml", "w") as f:
        f.write(rendered_template_bst)

    # TEST LANGUAGE
    template_test = get_template("test_lang.yaml.j2")

    rendered_template_test = template_test.render(jobs=jobs)
    with open("./.github/workflows/test_lang.yml", "w") as f:
        f.write(rendered_template_test)


if __name__ == "__main__":
    main()
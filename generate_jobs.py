from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml
from jinja2 import Environment, FileSystemLoader, Template
from requests import get
from yaml.loader import SafeLoader

from app import Job, get_jobs


@dataclass
class TestData:
    name: int
    lenght: int
    height: int


def get_env() -> Environment:
    return Environment(loader=FileSystemLoader("templates/"))


def get_template(name: str) -> Template:
    env = get_env()
    template = env.get_template(name)
    return template


def main() -> None:
    jobs = get_jobs()
    languages = [job.language for job in jobs]
    test_data_collection = [
        TestData(name=1, lenght=2, height=2),
        TestData(name=2, lenght=5, height=4),
        TestData(name=3, lenght=15, height=7),
        TestData(name=4, lenght=500, height=19),
    ]
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
    attempts = str(list(range(1, 6)))

    # BST jobs
    template_bst = get_template("main.yaml.j2")

    rendered_template_bst = template_bst.render(
        jobs=jobs, amount=amount, attempts=attempts, languages=languages
    )
    with open("./.github/workflows/main.yaml", "w") as f:
        f.write(rendered_template_bst)

    # TEST LANGUAGE
    template_test = get_template("test_lang.yaml.j2")

    for job in jobs:
        rendered_template_test = template_test.render(
            job=job, test_data_collection=test_data_collection
        )
        with open(
            f"./.github/workflows/test_lang-{job.language}.yaml", "w"
        ) as f:
            f.write(rendered_template_test)


if __name__ == "__main__":
    main()

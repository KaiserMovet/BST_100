import json
import sys
from pathlib import Path

from app import CONF_JSON, Job, Result, ResultCollection, get_jobs


def generate_results(results_path):
    results = []
    print(f"Checking path {results_path}")

    for result_txt in results_path.glob("*.txt"):
        file_name = result_txt.stem
        print(f"Loading {file_name}")
        lan_name = file_name.split("-")[1]
        amount = int(file_name.split("-")[2])
        content = result_txt.read_text()
        result = Result.FROM_RESULT(lan_name, amount, content)
        results.append(result)

    rc = ResultCollection(results)
    rc.plot_all()
    rc.to_json(merge_with_existing=False)


def generate_conf_json():
    jobs = get_jobs()
    conf = {}
    for job in jobs:
        conf[job.language] = job.to_dict()
    with open(CONF_JSON, "w") as f:
        json.dump(conf, f)


def main():
    results_path = Path(sys.argv[1]).resolve()
    generate_results(results_path)
    generate_conf_json()


if __name__ == "__main__":
    main()

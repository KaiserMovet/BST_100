from pathlib import Path

from app import Result, ResultCollection


def main():
    results_path = Path("/temp/results").resolve()
    results = []
    for result_txt in results_path.glob("*.txt"):
        file_name = result_txt.stem
        lan_name = file_name.split("-")[1]
        amount = int(file_name.split("-")[2])
        content = result_txt.read_text()
        result = Result.FROM_RESULT(lan_name, amount, content)
        results.append(result)

    rc = ResultCollection(results)
    rc.plot_all()
    rc.to_json(merge_with_existing=False)


if __name__ == "__main__":
    main()

import sys

from app import Result, Runner


def main():
    lang = sys.argv[1]
    runner = Runner.FROM_FOLDER(lang)
    result = runner.run(100)
    print(result)

    res = None
    try:
        res = Result.FROM_RESULT(lang, 100, result)
    except Exception as e:
        print(e)
    print(res)
    if res and res.validation[1] != 14:
        print(f"Height should be 14. Currently is {res.validation[1]}")


if __name__ == "__main__":
    main()

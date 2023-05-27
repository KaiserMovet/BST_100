import sys
from pathlib import Path

from app import Result


def main():
    path = Path(sys.argv[1])
    content = path.read_text()
    result = Result.FROM_RESULT("test", 100, content)
    assert result.add
    assert result.check
    assert result.len
    assert result.height
    assert str(result.validation[0]) == 100


if __name__ == "__main__":
    main()

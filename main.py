from pathlib import Path

from app import Runner

r = Runner(
    image_name="gcc:12",
    container_name="sdds",
    app_path=Path("BST/c"),
    run_command="./main.out",
    build_command="g++ -std=c99 -o main.out main.c node.c tree.c",
)
a = r.run(100)
print(a)

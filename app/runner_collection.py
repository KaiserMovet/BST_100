from pathlib import Path

from .runner import Runner


class RunnerCollection:
    C = Runner(
        image_name="gcc:12",
        app_path=Path("BST/c"),
        run_command="./main.out",
        build_command="g++ -std=c99 -o main.out main.c node.c tree.c",
    )
    CPP = Runner(
        image_name="gcc:12",
        app_path=Path("BST/c++"),
        run_command="./main.out",
        build_command="g++ -o main.out main.cpp tree.cpp node.cpp",
    )
    PYTHON = Runner(
        image_name="python:3.11",
        app_path=Path("BST/python3"),
        run_command="python main.py",
    )
    RUST = Runner(
        image_name="rust:1.67",
        app_path=Path("BST/rust"),
        run_command="./main",
        build_command="rustc main.rs",
    )
    LUA = Runner(
        image_name="nickblah/lua:5",
        app_path=Path("BST/lua"),
        run_command="lua main.lua",
    )
    CS = Runner(
        image_name="mcr.microsoft.com/dotnet/sdk:5.0",
        app_path=Path("BST/c#"),
        run_command="dotnet run",
    )

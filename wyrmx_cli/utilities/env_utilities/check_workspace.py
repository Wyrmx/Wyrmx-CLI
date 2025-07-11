from pathlib import Path

import typer, sys, tomllib

def checkWorkspace():

    
    tomlFile = Path().cwd() / "pyproject.toml"

    if (
        not tomlFile.exists()
        or "tool" not in (data := tomllib.load(tomlFile.open("rb")))
        or "wyrmx" not in data["tool"]
    ):
        typer.secho("❌ Not a Wyrmx project: either this is not a valid Wyrmx workspace (missing `pyproject.toml`) or you are not in the project root directory.", fg="red")
        sys.exit(1)

from pathlib import Path

import typer, sys

def checkWorkspace():

    if not (Path().cwd() / "pyproject.toml").exists():
        typer.secho("❌ Not a Wyrmx project: either this is not a valid Wyrmx workspace (missing `pyproject.toml`) or you are not in the project root directory.", fg="red")
        sys.exit(1)
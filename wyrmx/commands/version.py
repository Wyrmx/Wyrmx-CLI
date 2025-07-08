from pathlib import Path
import tomllib
import typer

__version__ = "1.0.14"

def version(value: bool):
    typer.echo(f"Wyrmx CLI Version: {__version__}")
    raise typer.Exit()


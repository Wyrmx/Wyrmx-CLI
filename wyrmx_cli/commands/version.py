from pathlib import Path
import typer

__version__ = "1.0.23"

def version():
    typer.echo(f"Wyrmx CLI Version: {__version__}")
    raise typer.Exit()


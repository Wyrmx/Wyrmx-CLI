from pathlib import Path
import toml
import typer

def version(value: bool):
    pyproject = Path(__file__).parent.parent.parent / "pyproject.toml"
    parsed = toml.loads(pyproject.read_text())
    typer.echo(f"Wyrmx CLI Version: {parsed["project"]["version"]}")
    raise typer.Exit()


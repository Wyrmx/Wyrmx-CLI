from pathlib import Path
import typer

def fileExists(file: Path, filename: str, fileType: str):
    if file.exists():
        typer.echo(f"❌ {fileType} '{filename}' already exists.")
        raise typer.Exit(1)
    
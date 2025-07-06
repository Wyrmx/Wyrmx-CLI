import subprocess
import sys
import typer
from pathlib import Path

def new(project_name: str):


    def createProjectFolder(projectName: str):
        projectPath = Path(projectName)

        try:
            projectPath.mkdir(parents=True, exist_ok=False)
            typer.echo(f"Created project folder: {projectPath.resolve()}")
        except FileExistsError:
            typer.echo(f"Error: Folder '{projectName}' already exists.")


    def createVirtualEnvironment(projectName: str):
        projectPath = Path(projectName)

        subprocess.run(
            [sys.executable, "-m", "venv", str(projectPath)],
            check=True
        )


    """
    Create a new Wyrmx project.
    """
    projectName: str = project_name


    typer.echo(f"Initializing Wyrmx project: {projectName}")
    createProjectFolder(projectName)
    createVirtualEnvironment(projectName)
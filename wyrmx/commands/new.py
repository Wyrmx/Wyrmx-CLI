import subprocess
import sys
import textwrap
import typer

from pathlib import Path

def new(project_name: str):


    """
    Create a new Wyrmx project.
    """


    def createProjectFolder(projectName: str):
        projectPath = Path(projectName)

        try:
            projectPath.mkdir(parents=True, exist_ok=False)
            typer.echo(f"Created project folder: {projectPath.resolve()} ✅")
        except FileExistsError:
            typer.echo(f"Error: Folder '{projectName}' already exists.")


    def createVirtualEnvironment(projectName: str):
        projectPath = Path(projectName)

        subprocess.run(
            [sys.executable, "-m", "venv", str(projectPath)],
            check=True
        )
    
    def initializeDependencies(projectName: str):
        typer.echo(f"Initializing Poetry & pyproject.toml...", )
        projectPath = Path(projectName)

        try:
            subprocess.run(
                ["poetry", "init", "--no-interaction"],
                cwd=str(projectPath),
                check=True
            )

            for initialDependency in ["fastapi", "uvicorn"]: subprocess.run(
                ["poetry", "add", initialDependency],
                cwd=str(projectPath),
                check=True
            )

        except FileNotFoundError:

            typer.echo(
                "Error: Poetry is not installed.\n"
                "Install it with: `pip install poetry` or follow https://python-poetry.org/docs/#installation"
            )
            raise typer.Exit(1)
        

    
    def updateGitignore(projectName: str):
        gitignorePath = Path(projectName)/".gitignore"
        gitignorePath.write_text(
            textwrap.dedent("""\
                # Python virtual environment
                venv/
                bin/
                include/
                lib/
                lib64/
                local/
                pyvenv.cfg
                .env

                # Bytecode cache
                **/__pycache__/**
            """)
        )
    

    def initSourceCode(projectName: str):
        

        def createSrc():
            srcPath = Path(projectName)/"src"
            srcPath.mkdir(parents=True, exist_ok=True)
        
            for folder in ["controllers", "services", "models"] : (srcPath/folder).mkdir(parents=True, exist_ok=True)
        
        def createMain():
            mainPath = Path(projectName)/"src"/"main.py"

            template = (
                f"from fastapi import FastAPI\n"
                f"from wyrmx.router import bindRouters\n\n"
                f"app = FastAPI()\n"
                f"bindRouters(app)"
            )

            mainPath.write_text(template)
        
        def createEnv():

            for file in [".env", ".env.example"] : 
                path = Path(projectName) / file
                path.write_text("")
        

        createSrc()
        createMain()
        createEnv()

        
            

        



    projectName: str = project_name


    typer.echo(f"Initializing Wyrmx project: {projectName}")

    createProjectFolder(projectName)
    createVirtualEnvironment(projectName)
    initializeDependencies(projectName)
    updateGitignore(projectName)
    initSourceCode(projectName)
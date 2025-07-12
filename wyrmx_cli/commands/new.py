import subprocess
import textwrap
import typer

from pathlib import Path
from wyrmx_cli.utilities.file_utilities import insertLines, insertLine, replaceLines

def new(project_name: str):


    """
    Create a new Wyrmx project.
    """


    def createProjectFolder(projectName: str):
        projectPath = Path(projectName)

        try:
            projectPath.mkdir(parents=True, exist_ok=False)
            typer.secho(f"Created project folder: {projectPath.resolve()} ✅", fg=typer.colors.GREEN)
        except FileExistsError:
            typer.secho(f"Error: Folder '{projectName}' already exists.", fg=typer.colors.RED)


    
    def createReadmeMarkdown(projectName: str):

        try:
            readmeMarkdown = Path(projectName)/"README.md"
            readmeMarkdown.write_text("")

            typer.secho(f"Created README default documentation ✅", fg=typer.colors.GREEN)
        except FileExistsError:
            typer.secho(f"Error: File '{str(readmeMarkdown)}' already exists.", fg=typer.colors.RED)
    

    





    def createVirtualEnvironment(projectName: str):

        typer.echo(f"Initializing Poetry & pyproject.toml and creating virtual environment...")
        projectPath = Path(projectName)

        try :

            commands = [
                ["poetry", "init", "--no-interaction"],
                ["poetry", "config", "virtualenvs.in-project", "true"],
                ["poetry", "install", "--no-root"],
            ]

            for command in commands: subprocess.run(
                command,
                cwd=str(projectPath),
                check=True

            )
                
            insertLine(projectPath / "pyproject.toml", 40, "\n\n" + "[tool.wyrmx]\n" + 'type = "project"')
        
        except FileNotFoundError:

            typer.secho(
                "Error: Poetry is not installed.\n"
                "Install it with: `pip install poetry` or follow https://python-poetry.org/docs/#installation",
                fg=typer.colors.RED
            )
            raise typer.Exit(1)


    def initDependencies(projectName: str):
        typer.echo(f"Installing initial dependencies...", )

        projectPath = Path(projectName)

        try:

            for initialDependency in ["fastapi", "uvicorn", "wyrmx-core", "alembic", "python-dotenv"]: subprocess.run(
                ["poetry", "add", initialDependency],
                cwd=str(projectPath),
                check=True
            )

        except FileNotFoundError:

            typer.echo(
                "Error: Poetry is not installed.\n"
                "Install it with: `pip install poetry` or follow https://python-poetry.org/docs/#installation",
                fg=typer.colors.RED
            )
            raise typer.Exit(1)
        

    
    def updateGitignore(projectName: str):
        gitignorePath = Path(projectName)/".gitignore"
        gitignorePath.write_text(
            textwrap.dedent("""\
                # Python virtual environment
                .venv/
                bin/
                include/
                lib/
                lib64/
                local/
                pyvenv.cfg
                *.db
                .env

                # Bytecode cache
                **/__pycache__/**
            """)
        )
    

    def initSourceCode(projectName: str):
        

        def createSrc():
            srcPath = Path(projectName)/"src"
            srcPath.mkdir(parents=True, exist_ok=True)
        
            for folder in ["controllers", "services", "models", "schemas"] : (srcPath/folder).mkdir(parents=True, exist_ok=True)
        

        
        def createAppModule():
            appModulePath = Path(projectName)/"src"/"app_module.py"
            appModulePath.write_text("")

        
        def createMain():
            mainPath = Path(projectName)/"src"/"main.py"

            template = (

                f"from wyrmx_core import WyrmxAPP\n"
                f"from . import app_module\n\n"
                f"app = WyrmxAPP()"
            )

            mainPath.write_text(template)
        
        def createEnv():

            for file in [".env", ".env.example"] : 
                path = Path(projectName) / file
                path.write_text("")

            insertLine(Path(projectName)/".env.example", 0, "DATABASE_URL='database url'")
            insertLine(Path(projectName)/".env", 0, "DATABASE_URL=#database url")
        
        def createMigrationScript(): 

            projectPath = Path(projectName)

            subprocess.run(
                ["poetry", "run","alembic", "init", "-t", "generic" ,"src/migrations"],
                cwd=str(projectPath),
                check=True
            )

            typer.secho(f"Created Alembic ini file ✅", fg=typer.colors.GREEN)

            migrationScriptFile = projectPath / "src" / "migrations" / "env.py"

            insertLines(
                migrationScriptFile,
                {
                    0: "from wyrmx_core.db import DatabaseSchema\n" + "from dotenv import load_dotenv\n ",
                    9: "import os, sys\n\n" + "sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))\n" + "\nfrom src.schemas import *\n\n" + "load_dotenv()\n" ,
                    29: "\n" + "config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))\n"
                } 
            )

            replaceLines(
                migrationScriptFile,
                {
                   "target_metadata = None": "target_metadata = DatabaseSchema.metadata",
                   'url = config.get_main_option("sqlalchemy.url")' : "\n",
                   "url=url": "url=os.getenv('DATABASE_URL')"
                }
            )

            typer.echo(f"Created Database Migration script ✅")
            

        

        createSrc()
        createAppModule()
        createMain()
        createEnv()
        createMigrationScript()


        
            
    def initGit(projectName: str):

        subprocess.run(
            ["git", "init"],
            cwd=str(Path(projectName)),
            check=True
        )
        



    projectName: str = project_name


    typer.echo(f"Initializing Wyrmx project: {projectName}")

    createProjectFolder(projectName)
    createReadmeMarkdown(projectName)
    createVirtualEnvironment(projectName)
    initDependencies(projectName)
    updateGitignore(projectName)
    initSourceCode(projectName)
    initGit(projectName)
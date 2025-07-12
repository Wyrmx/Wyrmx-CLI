from pathlib import Path
import subprocess, typer



def make_migration(
    message: str = typer.Option(..., "-m", "--message", help="Migration message"),
    empty: bool = typer.Option(False, "-e", "--empty", help="Empty migration")
):

    """
    Create a new database migration based on your current schemas.
    """

    def createEmptyMigration():
        typer.secho("[INFO] Starting empty migration creation...", fg=typer.colors.GREEN)
        typer.secho(f"[INFO] Running: alembic revision -m \"{message}\"", fg=typer.colors.GREEN)
        subprocess.run(["alembic", "revision","-m", f"'{message}'"], cwd=str(Path().cwd()), check=True, capture_output=True, text=True) 


    def createMigration():
        typer.secho("[INFO] Starting migration creation...", fg=typer.colors.GREEN)
        typer.secho(f"[INFO] Running: alembic revision --autogenerate -m \"{message}\"", fg=typer.colors.GREEN)

        subprocess.run(["alembic", "revision","--autogenerate", "-m", f"'{message}'"], cwd=str(Path().cwd()), check=True, capture_output=True, text=True)

        



    try: 

        match empty :
            case True : createEmptyMigration()
            case False: createMigration()

        typer.secho("[INFO] Migration created successfully.", fg=typer.colors.GREEN)
    
    except subprocess.CalledProcessError as e:
        typer.secho(f"[ERROR] Migration creation failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)









    
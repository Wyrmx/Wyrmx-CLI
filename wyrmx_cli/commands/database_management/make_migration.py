from pathlib import Path
import subprocess, typer



def make_migration(message: str = typer.Option(..., "-m", "--message", help="Migration message")):

    """
    Create a new database migration based on your current schemas.
    """

    typer.secho("[INFO] Starting migration creation...", fg=typer.colors.GREEN)
    typer.secho(f"[INFO] Running: alembic revision --autogenerate -m \"{message}\"", fg=typer.colors.GREEN)

    try: 
        subprocess.run(
            ["alembic", "revision","--autogenerate", "-m", f"'{message}'"],
            cwd=str(Path().cwd()),
            check=True,
            capture_output=True,
            text=True
        )

        typer.secho("[INFO] Migration created successfully.", fg=typer.colors.GREEN)
    
    except subprocess.CalledProcessError as e:
        typer.secho(f"[ERROR] Migration creation failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)









    
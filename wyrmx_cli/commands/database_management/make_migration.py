from pathlib import Path
import subprocess, typer



def make_migration(message: str = typer.Option(..., "-m", "--message", help="Migration message")):

    """
    Create a new database migration based on your current schemas.
    """

    typer.secho("[INFO] Starting migration creation...", fg=typer.colors.GREEN)
    typer.secho(f"[INFO] Running: alembic revision --autogenerate -m \"{message}\"", fg=typer.colors.GREEN)

    subprocess.run(
        ["alembic", "revision","--autogenerate", "-m", f"'{message}'"],
        cwd=str(Path().cwd()),
        stdout=subprocess.DEVNULL,
        check=True
    )

    typer.secho("[INFO] Migration created successfully.", fg=typer.colors.GREEN)









    
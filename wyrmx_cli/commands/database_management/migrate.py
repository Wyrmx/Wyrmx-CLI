from pathlib import Path
import subprocess, typer


def migrate(): 

    """
        Apply all pending database migrations.
    """

    typer.secho("[INFO] Starting database migration...", fg=typer.colors.GREEN)
    typer.secho("[INFO] Running: alembic upgrade head", fg=typer.colors.GREEN)
    
    subprocess.run(
        ["alembic", "upgrade","head"],
        cwd=str(Path().cwd()),
        stdout=subprocess.DEVNULL,
        check=True
    )

    typer.secho("[INFO] Database migration completed successfully.", fg=typer.colors.GREEN)
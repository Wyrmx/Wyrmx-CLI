from pathlib import Path
import subprocess, typer


def migrate(): 

    """
        Apply all pending database migrations.
    """

    typer.secho("[INFO] Starting database migration...", fg=typer.colors.GREEN)
    typer.secho("[INFO] Running: alembic upgrade head", fg=typer.colors.GREEN)
    
    try: 
        subprocess.run(
            ["alembic", "upgrade","head"],
            cwd=str(Path().cwd()),
            check=True,
            capture_output=True,
            text=True
        )

        typer.secho("[INFO] Database migration completed successfully.", fg=typer.colors.GREEN)
    
    except subprocess.CalledProcessError as e:
        typer.secho(f"[ERROR] Migration failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)
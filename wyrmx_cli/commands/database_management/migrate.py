from pathlib import Path
import subprocess, typer


def migrate(
    revision: str = typer.Option(None, "--revision", help="Migrate to specific revision."),
): 

    """
    Apply all pending database migrations.
    """


    def migrateToLatest():
        typer.secho("[INFO] Migrating database to latest revision...", fg=typer.colors.GREEN)
        typer.secho("[INFO] Running: alembic upgrade head", fg=typer.colors.GREEN)
        subprocess.run(["alembic", "upgrade","head"], cwd=str(Path().cwd()), check=True, capture_output=True, text=True)
    
    def migrateToRevision(revision: str):
        typer.secho(f"[INFO] Migrating database to revision {revision}...", fg=typer.colors.GREEN)
        typer.secho(f"[INFO] Running: alembic upgrade {revision}", fg=typer.colors.GREEN)
        subprocess.run(["alembic", "upgrade", revision], cwd=str(Path().cwd()), check=True, capture_output=True, text=True)



    typer.secho("[INFO] Starting database migration...", fg=typer.colors.GREEN)

    try:

        match revision:
            case None: migrateToLatest()
            case _: migrateToRevision(revision)

        typer.secho("[INFO] Database migration completed successfully.", fg=typer.colors.GREEN)



    except subprocess.CalledProcessError as e:
        typer.secho(f"[ERROR] Migration failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)




    
from pathlib import Path
import subprocess, typer



def make_migration(migration_text: str = typer.Option(..., "-m", "--message", help="Migration message")):

    """
    Create a new database migration based on your current schemas.
    """

    subprocess.run(
        ["alembic", "revision","--autogenerate", "-m", f"'{migration_text}'"],
        cwd=str(Path().cwd()),
        check=True
    )
    
from pathlib import Path
import subprocess


def migrate(): 

    """
        Apply all pending database migrations.
    """
    
    subprocess.run(
        ["alembic", "upgrade","head"],
        cwd=str(Path().cwd()),
        check=True
    )
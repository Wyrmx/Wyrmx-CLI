from pathlib import Path
import subprocess, typer


def edit(revision: str):

    """
    Open and edit migration/revision file in an editor
    """

    try: 
        subprocess.run(
            ["alembic", "edit", revision], 
            cwd=str(Path().cwd()), 
            stdin=None, stdout=None, stderr=None,
            #check=True, capture_output=True, text=True
        )

    except subprocess.CalledProcessError as e: typer.secho(f"[ERROR] Opening migration file failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)

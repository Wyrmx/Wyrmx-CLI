from pathlib import Path
import subprocess, typer


def downgrade(steps: int = 1):

    """
    Downgrade the database schema.
    """

    typer.secho(f"[INFO] Starting downgrade of {steps} step(s)...", fg=typer.colors.YELLOW)

    try: 

        for i in range(steps):
            typer.secho(f"[INFO] Downgrading step {i+1} of {steps}...", fg=typer.colors.YELLOW)
            result = subprocess.run(
                ["alembic", "downgrade","-1"],
                cwd=str(Path().cwd()),
                check=True,
                capture_output=True,
                text=True
            )

        typer.secho(f"[INFO] Downgrade completed: {steps} step(s) downgraded.", fg=typer.colors.GREEN)

    except subprocess.CalledProcessError as e:
        typer.secho(f"[ERROR] Migration failed at step {i+1}: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)

    
    

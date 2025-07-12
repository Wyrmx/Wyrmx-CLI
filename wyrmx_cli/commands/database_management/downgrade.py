from pathlib import Path
import subprocess, typer


def downgrade(
    steps: int = typer.Option(None, "--steps", help="Number of downgrade steps."),
    version: str = typer.Option(None, "--version", help="Downgrade to specific revision.")
):

    """
    Downgrade the database schema.
    """

    def downgradeToVersion(version: str): 

        try: 
            typer.secho(f"[INFO] Downgrading to revision {version}...", fg=typer.colors.YELLOW)

            subprocess.run(
                ["alembic", "downgrade", version],
                cwd=str(Path().cwd()),
                check=True,
                capture_output=True,
                text=True
            )

            typer.secho(f"[INFO] Downgrade to version {version} completed.", fg=typer.colors.GREEN)

        except subprocess.CalledProcessError as e:
            typer.secho(f"[ERROR] Downgrade to version {version} failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)
       

    def downgradeSteps(steps: int): 

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
            typer.secho(f"[ERROR] Downgrade failed at step {i+1}: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)




    if bool(steps) == bool(version): typer.secho("[ERROR] Use either --steps or --version (one required, not both).", fg=typer.colors.RED,)
    elif version: downgradeToVersion(version)
    else: downgradeSteps(1 if not bool(steps) else steps)

    

    
    

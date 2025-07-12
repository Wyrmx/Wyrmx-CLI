from pathlib import Path
import subprocess, typer


def rollback(
    steps: int = typer.Option(None, "--steps", help="Number of rollback steps."),
    revision: str = typer.Option(None, "--revision", help="Rollback to specific revision."),
    base: bool = typer.Option(False, "--base", help="Rollback all the way down to initial schema.")
):

    """
    Downgrade/Rollback the database schema.
    """

    def rollbackToBase():

        try: 
            typer.secho(f"[INFO] Rolling back to base schema...", fg=typer.colors.YELLOW)

            subprocess.run(
                ["alembic", "downgrade", "base"],
                cwd=str(Path().cwd()),
                check=True,
                capture_output=True,
                text=True
            )

            typer.secho(f"[INFO] Rolling back to base schema completed.", fg=typer.colors.GREEN)

        except subprocess.CalledProcessError as e:
            typer.secho(f"[ERROR] Rolling back to base schema failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)


    def rollbackToRevision(revision: str): 

        try: 
            typer.secho(f"[INFO] Rolling back to revision {revision}...", fg=typer.colors.YELLOW)

            subprocess.run(
                ["alembic", "downgrade", revision],
                cwd=str(Path().cwd()),
                check=True,
                capture_output=True,
                text=True
            )

            typer.secho(f"[INFO] Rolling back to revision {revision} completed.", fg=typer.colors.GREEN)

        except subprocess.CalledProcessError as e:
            typer.secho(f"[ERROR] Rolling back to revision {revision} failed: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)
       

    def rollbackBySteps(steps: int): 

        typer.secho(f"[INFO] Starting rollback of {steps} step(s)...", fg=typer.colors.YELLOW)

        try:

            for i in range(steps):
                typer.secho(f"[INFO] Rolling back step {i+1} of {steps}...", fg=typer.colors.YELLOW)
                result = subprocess.run(
                    ["alembic", "downgrade","-1"],
                    cwd=str(Path().cwd()),
                    check=True,
                    capture_output=True,
                    text=True
                )

            typer.secho(f"[INFO] Rollback completed: {steps} step(s) completed.", fg=typer.colors.GREEN)

        except subprocess.CalledProcessError as e:
            typer.secho(f"[ERROR] Rollback failed at step {i+1}: {e.stderr or e.stdout or "Unknown error"}", fg=typer.colors.RED)




    #if bool(steps) == bool(revision): typer.secho("[ERROR] Use either --steps or --revision (one required, not both).", fg=typer.colors.RED,)

    if sum(bool(parameter) for parameter in [steps, revision, base]) > 1: typer.secho("[ERROR] Use exactly one option: --steps OR --revision OR --base.", fg=typer.colors.RED,)
    
    elif revision: rollbackToRevision(revision)
    elif base: rollbackToBase()
    else: rollbackBySteps(1 if not bool(steps) else steps)

    

    
    

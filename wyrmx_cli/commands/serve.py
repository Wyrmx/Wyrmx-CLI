from pathlib import Path
from rich.console import Console

import typer
import subprocess, os, sys


def serve(
    app_module: str = typer.Option("src.main:app", "--app", "-a", help="The Python module and ASGI app to run (e.g., src.main:app)"),
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="The host/IP address to bind the server to"),
    port: int = typer.Option(8000, "--port", "-p", help="The port number to bind the server to"),
    workers: int = typer.Option(4, "--workers", "-w", help="Number of Gunicorn worker processes")
):

    """
    Run Wyrmx server in production mode.
    """
    
    try: 
        projectRoot = Path.cwd()
        if not (projectRoot / "src").exists(): raise RuntimeError(f"ERROR: No `src` in {projectRoot}. Run from your project root.")

        os.chdir(projectRoot)
        sys.path.insert(0, str(projectRoot))
            
        with Console().status("[bold green][INFO]🔍 Running static type check with Pyright..."):
            subprocess.run(
                [
                        "poetry",
                        "run",
                        "pyright"
                ],
                cwd=str(projectRoot),
                check=True
            )
    

        typer.secho("[INFO]  ✅ Type check passed. 🚀 Launching Wyrmx server in production mode...", fg=typer.colors.GREEN)
        subprocess.run(
            [
                "poetry", "run", "gunicorn", app_module,
                "-k", "uvicorn.workers.UvicornWorker",
                "--bind", f"{host}:{port}",
                "--workers", str(workers)
            ],
            cwd=str(projectRoot),
            check=True
        )

    except ChildProcessError: pass

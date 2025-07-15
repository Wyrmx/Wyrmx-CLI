from rich.console import Console
from pathlib import Path

import subprocess, os, sys
import typer


def run(
    app_module: str = "src.main:app",
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True
):

    """
    Run Wyrmx Server.
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
        
        typer.secho("[INFO]  ✅ Type check passed. 🚀 Starting Wyrmx server...", fg=typer.colors.GREEN)

        subprocess.run(
            ["poetry", "run", "uvicorn", app_module, "--host", host, "--port", str(port), "--reload" if reload else "--no-reload"],
            cwd=str(projectRoot),
            check=True
        )

    except ChildProcessError: pass


    
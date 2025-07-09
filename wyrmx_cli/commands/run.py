


def run(
    app_module: str = "src.main:app",
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True
):

    """
    Run Wyrmx Server.
    """
    from pathlib import Path
    import subprocess, os, sys


    projectRoot = Path.cwd()
    if not (projectRoot / "src").exists(): raise RuntimeError(f"ERROR: No `src` in {projectRoot}. Run from your project root.")

    os.chdir(projectRoot)
    sys.path.insert(0, str(projectRoot))
    
    #uvicorn.run(app_module, host=host, port=port, reload=reload)

    subprocess.run(
        ["uvicorn", app_module, "--host", host, "--port", str(port), "--reload" if reload else "--no-reload"],
        cwd=str(projectRoot),
        check=True
    )


    
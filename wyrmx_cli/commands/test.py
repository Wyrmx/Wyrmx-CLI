from pathlib import Path
import subprocess, os, sys


def test(
    app_module: str = "src.main:app",
    host: str = "127.0.0.1",
    port: int = 8000,
    reload: bool = True
):
    
    """
    Run Wyrmx Unit tests.
    """

    projectRoot = Path.cwd()
    if not (projectRoot / "src").exists(): raise RuntimeError(f"ERROR: No `src` in {projectRoot}. Run from your project root.")

    os.chdir(projectRoot)
    sys.path.insert(0, str(projectRoot))

    env = os.environ.copy()
    env["PYTHONPATH"] = "."

    subprocess.run(
        [
            "poetry",
            "run",
            "pytest"
        ],
        cwd=str(projectRoot),
        env=env,
        check=True
    )
from pathlib import Path
from typing import Annotated, List, Optional

import subprocess, os, sys, typer



def test(
    controller: bool = typer.Option(False, "--controller", help="Run controller tests only."),
    service: bool = typer.Option(False, "--service", help="Run service tests only."),
    model: bool = typer.Option(False, "--model", help="Run model tests only."),

    extra_args: Optional[List[str]] = typer.Argument(
        None, help="Extra arguments to pass to pytest (e.g. -v, -k test_x)"
    )
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


    command = ["poetry", "run", "pytest", *__extendCommand(controller, service, model)]
    if extra_args: command.extend(extra_args)
  
    try: subprocess.run(command, cwd=str(projectRoot), env=env, check=True)
    except subprocess.CalledProcessError: pass



def __extendCommand(
    controller: bool,
    service: bool,
    model: bool

)->list[str]:
    
    testPaths: list[str] = []

    match (controller, service, model):
        case (True, False, False): testPaths.append("src/controllers")
        case (False, True, False): testPaths.append("src/services")
        case (False, False, True): testPaths.append("src/models")
        case (False, False, False): return testPaths

        case _: raise typer.BadParameter("Please select only one of: --controller, --service or --model.")

    return testPaths
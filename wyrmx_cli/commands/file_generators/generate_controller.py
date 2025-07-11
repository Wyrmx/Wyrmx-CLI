from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *
from wyrmx_cli.utilities.env_utilities import checkWorkspace

import typer


def generate_controller(name: str):

    """
    Generate a new controller. (shortcut: gc)
    """
    
    def addImportToAppModule(controllerFilename: str, controllerName: str):
        createFile(Path("src/app_module.py"))
        insertLine(Path("src/app_module.py"), 0, f"from .controllers.{controllerFilename} import {controllerName}\n")


    checkWorkspace()
        
    controllerBasename = camelcase(name)
    controllerName = pascalcase(name, "Controller")
    controllerFilename = snakecase(name, "_controller")


    template = (
        f"from wyrmx_core import controller\n\n"
        f"@controller('{controllerBasename}')\n"
        f"class {controllerName}:\n\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )

    controllerFolder = Path().cwd() / "src" / "controllers"
    controllerFolder.mkdir(parents=True, exist_ok=True)

    controller = controllerFolder / f"{controllerFilename}.py"
    fileExists(controller, controllerFilename, "Controller")

    controller.write_text(template)

    createFile(controllerFolder/"__init__.py")
    insertLine(controllerFolder/"__init__.py", 0, f"from src.controllers.{controllerFilename} import {controllerName}")

    addImportToAppModule(controllerFilename, controllerName)
    typer.secho(f"✅ Created controller: {controller.resolve()}", fg="green")
    








   
from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *

import typer


def generate_controller(name: str):

    """
    Generate a new controller. (shortcut: gc)
    """
    
    def addImportToAppModule(controllerFilename: str, controllerName: str):
        appModule = Path("src/app_module.py")
        importLine = f"from .controllers.{controllerFilename} import {controllerName}\n"
        with appModule.open("a") as f: f.write(importLine)


        
        
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
    addImportToAppModule(controllerFilename, controllerName)
    typer.echo(f"✅ Created controller: {controller.resolve()}")
    








   
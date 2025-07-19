from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *
from wyrmx_cli.utilities.env_utilities import checkWorkspace

from wyrmx_cli.commands.file_generators.generate_controller.create_root_controller_folder import createRootControllerFolder
from wyrmx_cli.commands.file_generators.generate_controller.create_controller_folder import createControllerFolder

import typer


def __addImportToAppModule(controllerFilename: str, controllerName: str):
    createFile(Path("src/app_module.py"))
    insertLine(Path("src/app_module.py"), 0, f"from .controllers.{controllerFilename}.{controllerFilename} import {controllerName}\n")
    


def generate_controller(name: str):

    """
    Generate a new controller. (shortcut: gc)
    """
    
    checkWorkspace()

    controllerFilename = snakecase(name, suffix="_controller")
    controllerName = pascalcase(name, suffix="Controller")

    rootControllerFolder = createRootControllerFolder(name)
    controllerFolder = createControllerFolder(name, rootControllerFolder)


    __addImportToAppModule(controllerFilename, controllerName)
    typer.secho(f"✅ Created controller: {(controllerFolder / f"{controllerFilename}.py").resolve() }", fg=typer.colors.GREEN)
        
    
    








   
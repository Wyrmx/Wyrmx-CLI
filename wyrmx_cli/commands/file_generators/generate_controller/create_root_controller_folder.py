from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *



def __updateModule(controllerClassName:str, rootControllerFolder: Path):
    controllerFilename = snakecase(controllerClassName, suffix="_controller")
    controllerName = pascalcase(controllerClassName, suffix="Controller")

    createFile(rootControllerFolder/"__init__.py")
    insertLine(rootControllerFolder/"__init__.py", 0, f"from src.controllers.{controllerFilename}.{controllerFilename} import {controllerName}")


def createRootControllerFolder(name: str) -> Path: 
    rootControllerFolder = Path().cwd() / "src" / "controllers"
    rootControllerFolder.mkdir(parents=True, exist_ok=True)
    __updateModule(name, rootControllerFolder)
    return rootControllerFolder
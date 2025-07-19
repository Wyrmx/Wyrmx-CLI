from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *


def __createControllerFile(name: str, controllerFolder: Path):
    controllerBasename = camelcase(name)
    controllerName = pascalcase(name, suffix="Controller")
    controllerFilename = snakecase(name, suffix="_controller")

    template = (
        f"from wyrmx_core import controller\n\n"
        f"@controller('{controllerBasename}')\n"
        f"class {controllerName}:\n\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )

    controller = controllerFolder / f"{controllerFilename}.py"
    fileExists(controller, controllerFilename, "Controller")

    controller.write_text(template)


def __createControllerTestFile(name: str, controllerFolder: Path):
    controllerFilename = snakecase(name, suffix="_controller")
    controllerName = pascalcase(name, suffix="Controller")

    testControllerName = pascalcase(name, prefix="Test" ,suffix="Controller")
    testControllerFilename = snakecase(name, prefix="test_", suffix="_controller")

    template = (
        f"import pytest\n"
        f"from src.controllers.{controllerFilename}.{controllerFilename} import {controllerName}\n\n"

        f"class {testControllerName}:\n\n"
        f"    @pytest.fixture(autouse=True)\n"
        f"    def setup(self): self.controller = {controllerName}()"
    )

    testController = controllerFolder / f"{testControllerFilename}.py"
    testController.write_text(template)



def __updateModule(controllerClassName:str, controllerFolder: Path):
    controllerFilename = snakecase(controllerClassName, suffix="_controller")
    controllerName = pascalcase(controllerClassName, suffix="Controller")

    createFile(controllerFolder/"__init__.py")
    insertLine(controllerFolder/"__init__.py", 0, f"from src.controllers.{controllerFilename}.{controllerFilename} import {controllerName}")




def createControllerFolder(name: str, rootControllerFolder: Path):
    controllerFolder = rootControllerFolder / snakecase(name, suffix="_controller")
    controllerFolder.mkdir(parents=True, exist_ok=True)

    __createControllerFile(name, controllerFolder)
    __createControllerTestFile(name, controllerFolder)
    __updateModule(name, controllerFolder)


    return controllerFolder
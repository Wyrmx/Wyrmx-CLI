from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *




def __createModelFile(name: str, modelFolder: Path):
    modelName = pascalcase(name)
    modelFilename = snakecase(name, suffix="_model")

    template = (
        f"from wyrmx_core import model\n"
        f"from wyrmx_core.db import Model\n\n"
        f"@model\n"
        f"class {modelName}(Model):\n\n"
        f"    __schema__ = None #Bind the schema that corresponds to this model\n\n"

        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )


    service = modelFolder / f"{modelFilename}.py"
    fileExists(service, modelFilename, "Service")

    service.write_text(template)



def __createModelTestFile(name: str, serviceFolder: Path):
    modelFilename = snakecase(name, suffix="_model")
    modelName = pascalcase(name)

    testModelName = pascalcase(name, prefix="Test")
    testModelFilename = snakecase(name, prefix="test_", suffix="_model")

    template = (
        f"import pytest\n"
        f"from src.models.{modelFilename}.{modelFilename} import {modelName}\n\n"

        f"class {testModelName}:\n\n"
        f"    @pytest.fixture(autouse=True)\n"
        f"    def setup(self): self.service = {modelName}()"
    )

    testModel = serviceFolder / f"{testModelFilename}.py"
    testModel.write_text(template)



def __updateModule(modelClassName:str, modelFolder: Path):
    modelFilename = snakecase(modelClassName, suffix="_model")
    modelName = pascalcase(modelClassName)

    createFile(modelFolder/"__init__.py")
    insertLine(modelFolder/"__init__.py", 0, f"from src.models.{modelFilename}.{modelFilename} import {modelName}")



def createModelFolder(name: str, rootModelFolder: Path):
    modelFolder = rootModelFolder / snakecase(name, suffix="_model")
    modelFolder.mkdir(parents=True, exist_ok=True)

    __createModelFile(name, modelFolder)
    __createModelTestFile(name, modelFolder)
    __updateModule(name, modelFolder)


    return modelFolder
from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *



def __updateModule(modelClassName:str, rootModelFolder: Path):
    modelFilename = snakecase(modelClassName, suffix="_model")
    modelName = pascalcase(modelClassName)

    createFile(rootModelFolder/"__init__.py")
    insertLine(rootModelFolder/"__init__.py", 0, f"from src.models.{modelFilename}.{modelFilename} import {modelName}")


def createRootModelFolder(name: str) -> Path: 
    rootModelFolder = Path().cwd() / "src" / "models"
    rootModelFolder.mkdir(parents=True, exist_ok=True)
    __updateModule(name, rootModelFolder)
    return rootModelFolder
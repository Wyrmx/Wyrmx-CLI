from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *



def __updateModule(serviceClassName:str, rootServiceFolder: Path):
    serviceFilename = snakecase(serviceClassName, suffix="_service")
    serviceName = pascalcase(serviceClassName, suffix="Service")

    createFile(rootServiceFolder/"__init__.py")
    insertLine(rootServiceFolder/"__init__.py", 0, f"from src.services.{serviceFilename}.{serviceFilename} import {serviceName}")


def createRootServiceFolder(name: str) -> Path: 
    rootServiceFolder = Path().cwd() / "src" / "services"
    rootServiceFolder.mkdir(parents=True, exist_ok=True)
    __updateModule(name, rootServiceFolder)
    return rootServiceFolder
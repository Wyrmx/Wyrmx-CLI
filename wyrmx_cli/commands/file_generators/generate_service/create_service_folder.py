from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *




def __createServiceFile(name: str, serviceFolder: Path):
    serviceName = pascalcase(name, suffix="Service")
    serviceFilename = snakecase(name, suffix="_service")

    template = (
        f"from wyrmx_core import service\n\n"
        f"@service\n"
        f"class {serviceName}:\n\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )


    service = serviceFolder / f"{serviceFilename}.py"
    fileExists(service, serviceFilename, "Service")

    service.write_text(template)



def __createServiceTestFile(name: str, serviceFolder: Path):
    serviceFilename = snakecase(name, suffix="_service")
    serviceName = pascalcase(name, suffix="Service")

    testServiceName = pascalcase(name, prefix="Test" ,suffix="Service")
    testServiceFilename = snakecase(name, prefix="test_", suffix="_service")

    template = (
        f"import pytest\n"
        f"from src.services.{serviceFilename}.{serviceFilename} import {serviceName}\n\n"

        f"class {testServiceName}:\n\n"
        f"    @pytest.fixture(autouse=True)\n"
        f"    def setup(self): self.service = {serviceName}()"
    )

    testService = serviceFolder / f"{testServiceFilename}.py"
    testService.write_text(template)



def __updateModule(serviceClassName:str, serviceFolder: Path):
    serviceFilename = snakecase(serviceClassName, suffix="_service")
    serviceName = pascalcase(serviceClassName, suffix="Service")

    createFile(serviceFolder/"__init__.py")
    insertLine(serviceFolder/"__init__.py", 0, f"from src.services.{serviceFilename}.{serviceFilename} import {serviceName}")



def createServiceFolder(name: str, rootServiceFolder: Path):
    serviceFolder = rootServiceFolder / snakecase(name, suffix="_service")
    serviceFolder.mkdir(parents=True, exist_ok=True)

    __createServiceFile(name, serviceFolder)
    __createServiceTestFile(name, serviceFolder)
    __updateModule(name, serviceFolder)


    return serviceFolder
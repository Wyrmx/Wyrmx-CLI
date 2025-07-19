from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *
from wyrmx_cli.utilities.env_utilities import checkWorkspace

from wyrmx_cli.commands.file_generators.generate_service.create_root_service_folder import createRootServiceFolder
from wyrmx_cli.commands.file_generators.generate_service.create_service_folder import createServiceFolder


import typer


def generate_service(name: str):

    """
    Generate a new service. (shortcut: gs)
    """

    checkWorkspace()

    serviceFilename = snakecase(name, suffix="_service")

    rootServiceFolder = createRootServiceFolder(name)
    serviceFolder = createServiceFolder(name, rootServiceFolder)

    typer.secho(f"✅ Created service: {(serviceFolder / f"{serviceFilename}.py").resolve()}", fg=typer.colors.GREEN)


    '''serviceName = pascalcase(name, suffix="Service")
    serviceFilename = snakecase(name, suffix="_service")


    template = (
        f"from wyrmx_core import service\n\n"
        f"@service\n"
        f"class {serviceName}:\n\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )

    serviceFolder = Path().cwd() / "src" / "services"
    serviceFolder.mkdir(parents=True, exist_ok=True)

    service = serviceFolder / f"{serviceFilename}.py"
    fileExists(service, serviceFilename, "Service")

    service.write_text(template)

    createFile(serviceFolder/"__init__.py")
    insertLine(serviceFolder/"__init__.py", 0, f"from src.services.{serviceFilename} import {serviceName}")'''

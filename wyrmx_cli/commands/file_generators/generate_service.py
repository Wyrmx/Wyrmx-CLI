from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *
from wyrmx_cli.utilities.env_utilities import checkWorkspace


import typer


def generate_service(name: str):

    """
    Generate a new service. (shortcut: gs)
    """

    checkWorkspace()

    serviceName = pascalcase(name, "Service")
    serviceFilename = snakecase(name, "_service")


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
    insertLine(serviceFolder/"__init__.py", 0, f"from src.controllers.{serviceFilename} import {serviceName}")

    typer.secho(f"✅ Created service: {service.resolve()}", fg="green")
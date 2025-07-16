from pathlib import Path

from wyrmx_cli.utilities.env_utilities.check_workspace import checkWorkspace
from wyrmx_cli.utilities.file_utilities import createFile, insertLine, fileExists
from wyrmx_cli.utilities.string_utilities import *


import typer



def generate_payload(name: str):

    """
    Generate a new http payload. (shortcut: gp)
    """

    checkWorkspace()

    payloadName = pascalcase(name, "Payload")
    payloadFilename = snakecase(name, "_payload")


    template = (
        f"from wyrmx_core import payload\n"
        f"from pydantic import BaseModel\n\n"

        f"@payload\n"
        f"class {payloadName}(BaseModel): pass\n\n"
    )


    payloadFolder = Path().cwd() / "src" / "payloads"
    payloadFolder.mkdir(parents=True, exist_ok=True)

    payload = payloadFolder / f"{payloadFilename}.py"
    fileExists(payload, payloadFilename, "Payload")


    payload.write_text(template)

    createFile(payloadFolder/"__init__.py")
    insertLine(payloadFolder/"__init__.py", 0, f"from src.payloads.{payloadFilename} import {payloadName}")

    typer.secho(f"✅ Created payload: {payload.resolve()}", fg=typer.colors.GREEN)
from pathlib import Path

from wyrmx_cli.utilities.env_utilities.check_workspace import checkWorkspace
from wyrmx_cli.utilities.file_utilities import createFile, insertLine, fileExists
from wyrmx_cli.utilities.string_utilities import *

import typer


def generate_response(name: str):


    """
    Generate a new http response. (shortcut: gr)
    """

    checkWorkspace()

    responseName = pascalcase(name, "Response")
    responseFilename = snakecase(name, "_response")


    template = (
        f"from wyrmx_core import response\n"
        f"from pydantic import BaseModel\n\n"

        f"@response\n"
        f"class {responseName}(BaseModel): pass\n\n"
    )

    responseFolder = Path().cwd() / "src" / "responses"
    responseFolder.mkdir(parents=True, exist_ok=True)

    payload = responseFolder / f"{responseFilename}.py"
    fileExists(payload, responseFilename, "Payload")


    payload.write_text(template)

    createFile(responseFolder/"__init__.py")
    insertLine(responseFolder/"__init__.py", 0, f"from src.responses.{responseFilename} import {responseName}")

    typer.secho(f"✅ Created response: {payload.resolve()}", fg=typer.colors.GREEN)
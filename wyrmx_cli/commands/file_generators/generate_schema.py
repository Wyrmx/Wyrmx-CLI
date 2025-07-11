from pathlib import Path
from wyrmx_cli.utilities.env_utilities import checkWorkspace
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *

import typer


def generate_schema(name: str):

    """
    Generate a new database schema. (shortcut: gsc)
    """

    checkWorkspace()    

    schemaName = pascalcase(name, "Schema")
    schemaFilename = snakecase(name, "_schema")

    
    template = (
        f"from wyrmx_core.db import DatabaseSchema\n"
        f"from wyrmx_core import schema\n\n"
        f"@schema\n"
        f"class {schemaName}(DatabaseSchema):\n\n"
        f"    __tablename__= '{pascalcase(name)}'\n\n"
        f"    #define columns here\n"
    )

    schemaFolder = Path().cwd() / "src" / "schemas"
    schemaFolder.mkdir(parents=True, exist_ok=True)

    schema = schemaFolder / f"{schemaFilename}.py"
    fileExists(schema, schemaFilename, "Schema")


    schema.write_text(template)

    createFile(schemaFolder/"__init__.py")
    insertLine(schemaFolder/"__init__.py", 0, f"from src.schemas.{schemaFilename} import {schemaName}")

    typer.secho(f"✅ Created schema: {schema.resolve()}", fg="green")
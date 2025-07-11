from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *
from wyrmx_cli.utilities.env_utilities import checkWorkspace


import typer



def generate_model(name: str):

    """
    Generate a new data model. (shortcut: gm)
    """
    
    checkWorkspace()

    modelName = pascalcase(name)
    modelFilename = snakecase(name)


    template = (
        f"from wyrmx_core import model\n\n"
        f"@model\n"
        f"class {modelName}:\n\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )

    modelFolder = Path().cwd() / "src" / "models"
    modelFolder.mkdir(parents=True, exist_ok=True)

    model = modelFolder / f"{modelFilename}.py"
    fileExists(model, modelFilename, "Model")

    model.write_text(template)

    createFile(modelFolder/"__init__.py")
    insertLine(modelFolder/"__init__.py", 0, f"from src.models.{modelFilename} import {modelName}")
    
    typer.secho(f"✅ Created model: {model.resolve()}", fg="green")
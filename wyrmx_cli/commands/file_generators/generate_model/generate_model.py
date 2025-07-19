from pathlib import Path
from wyrmx_cli.utilities.string_utilities import *
from wyrmx_cli.utilities.file_utilities import *
from wyrmx_cli.utilities.env_utilities import checkWorkspace


from wyrmx_cli.commands.file_generators.generate_model.create_root_model_folder import createRootModelFolder
from wyrmx_cli.commands.file_generators.generate_model.create_model_folder import createModelFolder


import typer



def generate_model(name: str):

    """
    Generate a new data model. (shortcut: gm)
    """
    
    #checkWorkspace()

    modelFilename = snakecase(name, suffix="_model")

    rootModelFolder = createRootModelFolder(name)
    modelFolder = createModelFolder(name, rootModelFolder)


    typer.secho(f"✅ Created model: {(modelFolder / f"{modelFilename}.py").resolve()}", fg=typer.colors.GREEN)



    '''template = (
        f"from wyrmx_core import model\n"
        f"from wyrmx_core.db import Model\n\n"
        f"@model\n"
        f"class {modelName}(Model):\n\n"
        f"    __schema__ = None #Bind the schema that corresponds to this model\n\n"

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
    insertLine(modelFolder/"__init__.py", 0, f"from src.models.{modelFilename} import {modelName}")'''
    
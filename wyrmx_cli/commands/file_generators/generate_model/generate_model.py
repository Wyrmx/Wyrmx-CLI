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
    
    checkWorkspace()

    modelFilename = snakecase(name, suffix="_model")

    rootModelFolder = createRootModelFolder(name)
    modelFolder = createModelFolder(name, rootModelFolder)


    typer.secho(f"✅ Created model: {(modelFolder / f"{modelFilename}.py").resolve()}", fg=typer.colors.GREEN)



    
    
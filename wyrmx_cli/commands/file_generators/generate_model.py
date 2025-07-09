from pathlib import Path
import re
import typer



def generate_model(name: str):

    """
    Generate a new data model. (shortcut: gm)
    """


    def pascalCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return "".join(word.capitalize() for word in name.split()) 
    
    def snakeCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower() + "_model"
    


    def fileExists(file: Path, filename: str, fileType: str):
        if file.exists():
            typer.echo(f"❌ {fileType} '{filename}' already exists.")
            raise typer.Exit(1)
    

    modelName = pascalCase(name)
    modelFilename = snakeCase(name)


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
    typer.echo(f"✅ Created model: {model.resolve()}")
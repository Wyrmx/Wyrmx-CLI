from pathlib import Path
import re

import typer


def generate_controller(name: str):

    """
    Generate a new controller.
    """


    def pascalCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return "".join(word.capitalize() for word in name.split()) + "Controller"
    
    def snakeCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower() + "_controller"

    def fileExists(file: Path, filename: str, fileType: str):
        if file.exists():
            typer.echo(f"❌ {fileType} '{filename}' already exists.")
            raise typer.Exit(1)
    
    controllerName = pascalCase(name)
    controllerFilename = snakeCase(name)


    template = (
        f"from wyrmx.core.decorators import controller\n\n"
        f"@controller\n"
        f"class {controllerName}:\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )


    controllerFolder = Path().cwd() / "src" / "controllers"
    controllerFolder.mkdir(parents=True, exist_ok=True)

    controller = controllerFolder / f"{controllerFilename}.py"
    fileExists(controller, controllerFilename, "Controller")

    controller.write_text(template)
    typer.echo(f"✅ Created controller: {controller.resolve()}")
    








   
from pathlib import Path
import re
import typer


def generate_controller(name: str):

    """
    Generate a new controller. (shortcut: gc)
    """

    def camelcase(name: str) -> str :
        name = re.sub(r"[-_]", " ", name)
        return "".join(word for word in name.split())


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
    
    def addImportToAppModule(controllerFilename: str, controllerName: str):
        appModule = Path("src/app_module.py")
        importLine = f"from .controllers.{controllerFilename} import {controllerName}\n"
        with appModule.open("a") as f: f.write(importLine)







        
        
    controllerBasePath = camelcase(name)
    controllerName = pascalCase(name)
    controllerFilename = snakeCase(name)


    template = (
        f"from wyrmx_core import controller\n\n"
        f"@controller('{controllerBasePath}')\n"
        f"class {controllerName}:\n\n"
        f"    def __init__(self):\n"
        f"        pass\n\n"
        f"    # Add your methods here\n"
    )


    controllerFolder = Path().cwd() / "src" / "controllers"
    controllerFolder.mkdir(parents=True, exist_ok=True)

    controller = controllerFolder / f"{controllerFilename}.py"
    fileExists(controller, controllerFilename, "Controller")

    controller.write_text(template)
    addImportToAppModule(controllerFilename, controllerName)
    typer.echo(f"✅ Created controller: {controller.resolve()}")
    








   
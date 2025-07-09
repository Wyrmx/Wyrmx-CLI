import re, typer
from pathlib import Path


def generate_service(name: str):

    """
    Generate a new service. (shortcut: gs)
    """


    def pascalCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return "".join(word.capitalize() for word in name.split()) + "Service"
    
    def snakeCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower() + "_service"

    def fileExists(file: Path, filename: str, fileType: str):
        if file.exists():
            typer.echo(f"❌ {fileType} '{filename}' already exists.")
            raise typer.Exit(1)
        
    serviceName = pascalCase(name)
    serviceFilename = snakeCase(name)


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
    typer.echo(f"✅ Created service: {service.resolve()}")
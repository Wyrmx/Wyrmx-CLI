from pathlib import Path
import re
import typer


def generate_schema(name: str):

    """
    Generate a new database schema. (shortcut: gsc)
    """


    def pascalCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return "".join(word.capitalize() for word in name.split())
    
    def snakeCase(name: str) -> str:
        name = re.sub(r"[-_]", " ", name)
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower() + "_schema"

    def fileExists(file: Path, filename: str, fileType: str):
        if file.exists():
            typer.echo(f"❌ {fileType} '{filename}' already exists.")
            raise typer.Exit(1)
    

    schemaName = pascalCase(name) + "Schema"
    schemaFilename = snakeCase(name)

    
    template = (
        f"from wyrmx_core import schema\n\n"
        f"@schema\n"
        f"class {schemaName}:\n\n"
        f"    __tablename__= '{pascalCase(name)}'\n\n"
        f"    #define columns here\n"
    )

    schemaFolder = Path().cwd() / "src" / "schemas"
    schemaFolder.mkdir(parents=True, exist_ok=True)

    schema = schemaFolder / f"{schemaFilename}.py"
    fileExists(schema, schemaFilename, "Schema")

    schema.write_text(template)
    typer.echo(f"✅ Created schema: {schema.resolve()}")
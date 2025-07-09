import typer
from wyrmx_cli.commands import build, new, run, version as ver
from wyrmx_cli.commands.file_generators import generate_controller, generate_service, generate_model, generate_schema
from wyrmx_cli.commands.database_management import make_migration, migrate

app = typer.Typer()
shortcuts = typer.Typer()


app.command()(build)
app.command()(new)
app.command()(run)

app.command("generate:controller")(generate_controller)
app.command("generate:service")(generate_service)
app.command("generate:model")(generate_model)
app.command("generate:schema")(generate_schema)
app.command("make:migration")(make_migration)
app.command("migrate")(migrate)


# Aliases — hidden at root level
app.command("gc", hidden=True)(generate_controller)
app.command("gs", hidden=True)(generate_service)
app.command("gm", hidden=True)(generate_model)
app.command("gsc", hidden=True)(generate_schema)



@app.callback(invoke_without_command=True)
def main( version: bool = typer.Option( None, "--version", is_eager=True, help="Show the Wyrmx CLI version.")): 
    if version: ver()


if __name__ == "__main__":
    app()


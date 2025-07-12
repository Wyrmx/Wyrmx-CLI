import typer
from wyrmx_cli import commands
from wyrmx_cli.commands.file_generators import *
from wyrmx_cli.commands.database_management import *

app = typer.Typer()
shortcuts = typer.Typer()

# main commands
app.command()(commands.build)
app.command()(commands.new)
app.command()(commands.run)

# file generation commands
app.command("generate:controller")(generate_controller)
app.command("generate:service")(generate_service)
app.command("generate:model")(generate_model)
app.command("generate:schema")(generate_schema)

# database migration commands
app.command("migration:make")(make_migration)
app.command("migration:apply")(migrate)
app.command("migration:rollback")(rollback)
app.command("migration:edit")(edit)


# Aliases — hidden at root level
app.command("gc", hidden=True)(generate_controller)
app.command("gs", hidden=True)(generate_service)
app.command("gm", hidden=True)(generate_model)
app.command("gsc", hidden=True)(generate_schema)



@app.callback(invoke_without_command=True)
def main( version: bool = typer.Option( None, "--version", "--v", is_eager=True, help="Show Wyrmx CLI version.")): 
    if version: commands.version()


if __name__ == "__main__":
    app()


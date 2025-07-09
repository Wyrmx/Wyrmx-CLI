import typer
from wyrmx_cli.commands import build, new, run, version as ver
from wyrmx_cli.commands.file_generators import generate_controller, generate_service, generate_model

app = typer.Typer()
shortcuts = typer.Typer()


app.command()(build)
app.command()(new)
app.command()(run)

app.command("generate:controller")(generate_controller)
app.command("generate:service")(generate_service)
app.command("generate:model")(generate_model)


# Aliases — hidden at root level
app.command("gc", hidden=True)(generate_controller)
app.command("gs", hidden=True)(generate_service)
app.command("gm", hidden=True)(generate_model)



@app.callback(invoke_without_command=True)
def main( version: bool = typer.Option( None, "--version", is_eager=True, help="Show the application version and exit.")): 
    if version: ver()


if __name__ == "__main__":
    app()


import typer
from typing import Optional
from wyrmx.commands import build, new, run, version
from wyrmx.commands.file_generators import generate_controller, generate_service

app = typer.Typer()

@app.callback()
def main( version: Optional[bool] = typer.Option( None, "--version", callback=version, is_eager=True, help="Show the application version and exit.")): pass

app.command()(build)
app.command()(new)
app.command()(run)

app.command("generate:controller")(generate_controller)
app.command("gc")(generate_controller)



app.command("generate:service")(generate_service)
app.command("gs")(generate_service)


if __name__ == "__main__":
    app()


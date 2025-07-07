import typer
from wyrmx.commands import build, new
from wyrmx.commands.file_generators import generate_controller

app = typer.Typer()

app.command()(build.build)
app.command()(new.new)

app.command()(generate_controller.generate_controller)



if __name__ == "__main__":
    app()
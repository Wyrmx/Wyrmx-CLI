import typer
from wyrmx.commands import build, new, run
from wyrmx.commands.file_generators import generate_controller, generate_service

app = typer.Typer()

app.command()(build.build)
app.command()(new.new)
app.command()(run.run)

app.command()(generate_controller.generate_controller)
app.command()(generate_service.generate_service)



if __name__ == "__main__":
    app()
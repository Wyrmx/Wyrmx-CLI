import typer
from wyrmx.commands import build, new, run
from wyrmx.commands.file_generators import generate_controller, generate_service

app = typer.Typer()

app.command()(build.build)
app.command()(new.new)
app.command()(run.run)

app.command("generate:controller")(generate_controller.generate_controller)
app.command("gc")(generate_controller.generate_controller)



app.command("generate:service")(generate_service.generate_service)
app.command("gs")(generate_service.generate_service)



if __name__ == "__main__":
    app()
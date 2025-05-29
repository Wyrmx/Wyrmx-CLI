import typer
from src.commands import build, new

app = typer.Typer()

app.command()(build.build)
app.command()(new.new)


if __name__ == "__main__":
    app()
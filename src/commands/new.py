import typer


def new(project_name: str):
    """
    Create a new Wyrmx project.
    """
    typer.echo(f"Initializing Wyrmx project: {project_name}")
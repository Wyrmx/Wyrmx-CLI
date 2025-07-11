from pathlib import Path


def createFile(path: Path):
    """
    Create a file if it does not exist
    """

    try:
        path.read_text()
    except FileNotFoundError:
        path.write_text("")

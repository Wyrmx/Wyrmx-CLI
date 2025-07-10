from pathlib import Path


def replaceLine(filePath: Path, oldText: int, newText: str):
    filePath.write_text(filePath.read_text().replace(oldText, newText))


def replaceLines(filePath: Path, replacements: dict[str, str]):
    for key, value in replacements.items(): replaceLine(filePath, key, value)
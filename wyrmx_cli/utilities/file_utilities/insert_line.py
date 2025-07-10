from pathlib import Path

def insertLine(filePath: Path, lineNumber: int, text: str):
    lines = filePath.read_text().splitlines()
    lines.insert(lineNumber, text)
    filePath.write_text('\n'.join(lines) + '\n')


def insertLines(filePath: Path, lines: dict[int, str]):
    for key, value in lines.items(): insertLine(filePath, key, value)
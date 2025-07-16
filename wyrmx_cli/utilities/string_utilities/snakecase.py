import re


def snakecase(name: str, suffix: str = "") -> str:
    name = re.sub(r"(?<!^)(?=[A-Z])", "_", name)
    name = re.sub(r"[-\s]", "_", name)
    return name.lower() + suffix

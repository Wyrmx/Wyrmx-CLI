import re


def snakecase(name: str, prefix: str = "", suffix: str = "") -> str:
    name = re.sub(r"(?<!^)(?=[A-Z])", "_", name)
    name = re.sub(r"[-\s]", "_", name)
    return prefix + name.lower() + suffix

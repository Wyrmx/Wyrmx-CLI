import re


def snakecase(name: str, suffix: str = "") -> str:
    name = re.sub(r"[-_]", " ", name)
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower() + suffix
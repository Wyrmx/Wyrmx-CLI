import re


def pascalcase(name: str, suffix: str = "") -> str:
    name = re.sub(r"[-_]", " ", name)
    return "".join(word.capitalize() for word in name.split()) + suffix
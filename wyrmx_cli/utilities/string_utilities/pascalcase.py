import re


def pascalcase(name: str, prefix: str = "", suffix: str = "") -> str:
    name = re.sub(r"[-_]", " ", name)
    return prefix + "".join(word.capitalize() for word in name.split()) + suffix
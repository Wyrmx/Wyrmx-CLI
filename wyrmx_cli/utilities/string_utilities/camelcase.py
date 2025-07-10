import re


def camelcase(name: str, suffix: str = "") -> str :
    name = re.sub(r"[-_]", " ", name)
    return "".join(word for word in name.split()) + suffix
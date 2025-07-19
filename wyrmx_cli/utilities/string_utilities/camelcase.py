import re


def camelcase(name: str, prefix: str = "", suffix: str = "") -> str :
    name = re.sub(r"[-_]", " ", name)
    return prefix + "".join(word for word in name.split()) + suffix
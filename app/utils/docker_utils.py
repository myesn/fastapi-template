import os


def is_docker() -> bool:
    return os.path.exists("/.dockerenv")


def is_not_docker() -> bool:
    return not is_docker()

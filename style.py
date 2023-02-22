from stringcolor import *


def unfocused(unstyled: str):
    return cs(unstyled, "grey")


def ok(unstyled: str):
    return cs(unstyled, "lime")


def spicy(unstyled: str):
    return bold(unstyled).cs("white", "darkorange")


def bad(unstyled: str):
    return bold(unstyled).underline().cs("black", "red")

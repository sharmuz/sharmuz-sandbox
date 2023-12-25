"""
Some trivial Python functions for testing purposes.
"""


def say_hello(friend: str = "stranger") -> str:
    """
    Prints a greeting to specified friend.

    Args:
        friend (str): Name of person being greeted.

    Returns:
        str: Greeting to friend.
    """
    return f"\nHello there, {friend}!\n"


def run():
    print(say_hello())


if __name__ == "__main__":
    run()

"""My 'first' COMP110 website."""

__author__ = "730699792"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


greet(name="Campers")
greet(name="Kris")


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))

"""COMP110's implementation of Wordle."""

__author__: str = "123456789"


def contains_char(word: str, ch: str) -> bool:
    """Checking if char 'ch' is in string 'word'."""
    assert len(ch) == 1, f"len({ch}) is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == ch:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Convert guess into a string of box emojis"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            output += GREEN_BOX
        elif contains_char(word=secret, ch=guess[i]):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        i += 1
    return output


def input_guess(ex_len: int) -> str:
    """Getting a guess from the user of the correct length."""
    guess = input("Enter a " + str(ex_len) + " character word:")
    while len(guess) != ex_len:
        guess = input("That wasn't " + str(ex_len) + " chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    guess: str = ""
    while turn < 6 and guess != secret:
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(ex_len=len(secret))
        print(emojified(guess=guess, secret=secret))
    if turn < 6:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

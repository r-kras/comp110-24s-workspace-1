"""Makes a tea party for the COMP110 crew."""

__author__: str = "1234567890"


def tea_bags(people: int) -> int:
    """Gets a number of tea bags proportional to the number of people."""
    return people * 2


def treats(people: int) -> int:
    """Gets a number of treats proportional to the number of people."""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the cost of the tea party."""
    return tea_count * 0.5 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """Bringing all the planning together."""
    print("A Cozy Tea Party for " + str(guests) + "people")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

"""Calculating grades for COMP110."""

__author__: str = "123456789"

Scores = tuple[float, ...]
"""Scores is a tuple of floats representing percent credit from 0.0 to 1.0."""

EX: Scores = (40.0 / 100.0, 102.0 / 100.0)
RD: Scores = (80.0 / 100.0, 75.0 / 100.0, 90.0 / 100.0)
LS: Scores = (100.0 / 100.0, 80.0 / 100.0, 50.0 / 100.0)
CL: Scores = (105.0 / 100.0, 100.0 / 100.0, 100.0 / 100.0)
QZ: Scores = (100.0 / 100.0, 93.0 / 100.0, 100.0 / 100.0, 93.0 / 100.0)
FN: float = 0.85
"""Exercise, Reading, Lesson, Clarity, Quiz, and Final scores."""


def average(work: Scores) -> float:
    """Determines the average of a tuple."""
    if len(work) == 0:
        return 0.0
    else:
        return sum(work) / len(work)


def ppp_components(ex: Scores, rd: Scores, ls: Scores, cl: Scores) -> float:
    """Calculates the ppp portion of the grade."""
    EX_WEIGHT: float = 0.25
    RD_WEIGHT: float = 0.05
    LS_WEIGHT: float = 0.05
    CL_WEIGHT: float = 0.05
    return (
        (average(ex) * EX_WEIGHT)
        + (average(rd) * RD_WEIGHT)
        + (average(ls) * LS_WEIGHT)
        + (average(cl) * CL_WEIGHT)
    )


def quiz_average(qz: Scores, fn: float) -> float:
    """Quiz averges with final considered."""
    if len(qz) == 0:
        return fn
    else:
        if min(qz) < fn:
            return (sum(qz) - min(qz) + fn) / len(qz)
        else:
            return average(qz)


def mastery_components(qz: Scores, fn: float) -> float:
    """Calculates the mastery portion of the grade."""
    QZ_WEIGHT: float = 0.4
    FN_WEIGHT: float = 0.2
    return (QZ_WEIGHT * quiz_average(qz, fn)) + (FN_WEIGHT * fn)


def count_zeros(qz: Scores, count: int = 0, i: int = 0) -> int:
    """Recursively iterates through qz to count number of zeros in function."""
    if len(qz) <= i:
        return count
    else:
        if qz[i] == 0.0:
            count = count + 1
        return count_zeros(qz, count, i + 1)


def has_min_mastery(qz: Scores, fn: float) -> bool:
    """Determines if minimum mastery of course is met."""
    return len(qz) >= 4 and count_zeros(qz) <= 1 and fn >= 0.4


def letter_grade(total: float, has_min_mastery: bool) -> str:
    """Gives the letter grade based on the student's grade and mastery."""
    total = total * 100
    if not has_min_mastery or total < 60:
        return "F"
    elif total >= 92.5:
        return "A"
    elif total >= 89.5:
        return "A-"
    elif total >= 86.5:
        return "B+"
    elif total >= 82.5:
        return "B"
    elif total >= 79.5:
        return "B-"
    elif total >= 76.5:
        return "C+"
    elif total >= 72.5:
        return "C"
    elif total >= 69.5:
        return "C-"
    else:
        return "D"


def calculate_grade(
    ex: Scores, rd: Scores, ls: Scores, cl: Scores, qz: Scores, fn: float
) -> str:
    """Produces a final grade calculation."""
    grade: float = ppp_components(EX, RD, LS, CL) + mastery_components(QZ, FN)
    return (
        "Final Grade: "
        + letter_grade((grade), has_min_mastery(QZ, FN))
        + " ("
        + str(round(grade * 100))
        + "%)"
    )


if __name__ == "__main__":
    print(calculate_grade(ex=EX, rd=RD, ls=LS, cl=CL, qz=QZ, fn=FN))

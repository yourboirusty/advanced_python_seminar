def isEven(x):
    if x % 2 == 0:
        return True
    return False


def isUpper(x):
    return x.isupper()

def square(x):
    return x**2


def grade(x):
    if x >= 95:
        return "5.5"
    elif x >= 80:
        return "5"
    elif x >= 70:
        return "4"
    elif x >= 65:
        return "3"
    elif x >= 50:
        return "2.5"
    return "2"


def main():
    nums = (1, 8, 12, 54, 199, 24566, 9, 35)
    chars = "yoUCaNTJuSTdoIT"
    grades = (5, 30, 68, 50, 100, 87, 76)

    # TODO Filter out odd numbers from nums
    evens = list(filter(isEven, nums))
    print(evens)

    # TODO Filter out lowercase from chars
    upeper = list(filter(isUpper, chars))
    print(upeper)

    # TODO Square all the nums
    squares = list(map(square, nums))
    print(squares)
    # TODO Sort and grade
    grades = sorted(grades)
    print(grades)
    real_grades = list(map(grade, grades))
    print(real_grades)


if __name__ == "__main__":
    main()
def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_pl = ["Nd", "Pon", "Wt", "Śr", "Czw", "Pt", "Sob"]

    # # TODO Use iter to go over days
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # # TODO Iterate with a counter
    # for day, i in enumerate(days, start=1):
    #     print(day, i)
    # print(next(enumerate(days, start=1)))
    # # TODO Combine sequences
    # for day in zip(days, days_pl):
    #     print(day[0] + ": " + day[1])

    # TODO Use a function with a sentinel

    with open("iter.txt", "r") as fp:
        for line in iter(fp.readline, "# This is line 5\n"):
            print(line)


if __name__ == "__main__":
    main()

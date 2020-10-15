import itertools


def testFunc(x):
    return x > 0


def main():
    # TODO Cycle over the week infinitely
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # cycle = itertools.cycle(days)
    # for _ in range(10):
    #     print(next(cycle))

    # TODO Create a simple counter
    vals = list()
    count = itertools.count(-30, 10)
    for _ in range(10):
        vals.append(next(count))
    print(vals)

    # TODO Print values until a condition is met
    itertools.dropwhile(testFunc, vals)
    itertools.takewhile(testFunc, vals)

if __name__ == "__main__":
    main()

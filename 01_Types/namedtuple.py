from collections import namedtuple


def main():
    # TODO Define a point
    Point = namedtuple("Point", "x y")

    p1 = Point(20,30)
    p2 = Point(-5, 20)

    print(p1, p2)
    print(p1.x, p2.y)

    p1 = p1._replace(x=1)
    print(p1.x)


if __name__ == "__main__":
    main()
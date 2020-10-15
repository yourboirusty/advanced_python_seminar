def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ftemps = [16, 35, 66, 109, 234]

    # TODO: Map regular function to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))

    # TODO: Oneline that stuff
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))


if __name__ == "__main__":
    main()
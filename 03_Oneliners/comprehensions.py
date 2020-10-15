# km = mile * 1.6


def main():
    distances = [50, 24, 100, 120, 50] #in miles

    # TODO Create a matrix with kms
    distance_in_km = [x * 1.6 for x in distances if x > 50]
    print(distance_in_km)

    # TODO Create a dict with both values
    distance_dict = {x: y for x, y in zip(distances, distance_in_km)}
    print(distance_dict)

    # TODO Create a set with kms
    

if __name__ == "__main__":
    main()

from collections import defaultdict


def main():
    items = ["dagger", "knife", "halberd", "picklock", "picklock",
             "picklock", "scrap", "useless_potion", "useless_potion"]
    backpack = defaultdict(int)

    # TODO Count items transfered into backpack
    for item in items:
        backpack[item] += 1
    
    print(backpack)


if __name__ == "__main__":
    main()
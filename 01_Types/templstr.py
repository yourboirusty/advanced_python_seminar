from string import Template


def main():
    # The usual
    str1 = "We are working on {0} with {1}".format("Advanced python", "Kornel")
    print(str1)

    # Template
    templ = Template("Przerabiamy teraz ${title} z ${author}")

    # TODO Actually use the template

    # TODO Templates for bigger datasets


if __name__ == "__main__":
    main()

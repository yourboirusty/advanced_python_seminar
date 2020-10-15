from string import Template


def main():
    # The usual
    str1 = "We are working on {0} with {1}".format("Advanced python", "Kornel")
    str2 = "Test" + "test2"
    print(str2)
    print(str1)

    # Template
    templ = Template("Przerabiamy teraz ${title} z ${author}")

    # TODO Actually use the template
    str3 = templ.substitute(title="Advanced Python", author = "Kornel")
    print(str3)

    # TODO Templates for bigger datasets
    data = {
        "author": "Kornel",
        "title": "Advanced Python"
    }
    str4 = templ.substitute(data)
    print(str4)


if __name__ == "__main__":
    main()

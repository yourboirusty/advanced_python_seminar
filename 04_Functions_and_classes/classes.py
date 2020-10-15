# TODO Make this class printable and easier to debug
class MyClass:
    shared_property = "some_property"

    def __init__(self, other_property, named_property="test"):
        self.other_property = other_property
        self.named_property = named_property

    def __str__(self):
        return "{0}, {1}".format(self.shared_property,
                                 self.other_property
                                 )

    # def __repr__(self):
    #     return "{0}, {1}: {2}".format(self.shared_property,
    #                             self.other_property,
    #                             self.named_property
    #                             )


# TODO Add dynamic attributes and documentation
class RGBClass:

    def __init__(self):
        self.red = 10
        self.blue = 75
        self.green = 100

    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.blue, self.green)
        raise AttributeError

    def __dir__(self):
        return ('rgbcolor')



if __name__ == "__main__":
    RGB = RGBClass()
    print(RGB.rgbcolor)
    print(RGB.asdf)

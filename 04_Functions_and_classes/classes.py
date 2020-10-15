# TODO Make this class printable and easier to debug
class MyClass:
    shared_property = "some_property"

    def __init__(self, other_property, named_property="test"):
        self.other_property = other_property
        self.named_property = named_property


# TODO Add dynamic attributes and documentation
class RGBClass:

    def __init__(self):
        self.red = 10
        self.blue = 75
        self.green = 100

from mammal import Mammal

# Lab 12 - Child can inherit only public fields from the parent
class Person(Mammal):
    def __init__(self, p_name, p_age, p_height):
        super().__init__(p_age)  # ✅ Use super() for proper inheritance
        print("Constructor: Adding the Person parts of a person")

        # Set Person-specific fields
        self.name = p_name
        self.age = p_age  # ✅ Ensure Person class explicitly has an age attribute
        self.__height = p_height

    def __del__(self):
        print("Destructor: The garbage collector is now deleting the person object")
        super().__del__()

    # Complex getter for height
    @property
    def height(self):
        return self.__height

    # Complex setter for height
    @height.setter
    def height(self, p_height):
        self.__height = p_height

    # Overridden method
    def love(self):
        print("This human is feeling love in a more complex emotional way...")

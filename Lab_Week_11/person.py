# person.py

class Person:
    # Constructor
    def __init__(self, name, age, height):
        print("Constructing the Person object")
        # Private attributes using double underscore
        self.__name = name
        self.__age = age
        self.__height = height
        # Public attribute
        self.public_prop = "I'm public"

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, new_name):
        self.__name = new_name

    # Destructor
    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

# Testing the Person class
if __name__ == "__main__":
    # Create an instance
    person1 = Person("Mark", 20, 6)

    # Accessing the public property
    print("Public Property:", person1.public_prop)  # This will work

    try:
        print("Private Property:", person1.__name)  # Will raise AttributeError
    except AttributeError as e:
        print("Error accessing private attribute:", e)

    # Using getter and setter
    # print("Name using getter:", person1.get_name())
    # person1.set_name("Anna")
    # print("Updated name using setter:", person1.get_name())

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    print("Name using property:", person1.name)
    person1.name = "Anna"
    print("Updated name using property:", person1.name)

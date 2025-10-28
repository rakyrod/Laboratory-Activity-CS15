class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("WOOF WOOF")

    def Dog_Birthday(self):
        self.age = self.age + 1
        print("Happy Birthday!", self.name, "is now", self.age, "years old.")

    def get_info(self):
        print("Dog Name:", self.name, "Age:", self.age)


# Create a Dog object
my_dog = Dog("Max,", 5)

# Call the methods
my_dog.bark()
my_dog.Dog_Birthday()
my_dog.get_info()

class Dog:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.color} {self.breed}.")

my_dog = Dog("Buddy", 3, "brown", "Golden Retriever")
my_dog.sit()
my_dog.roll_over()
my_dog.describe()
class User:
    def __init__(self, first_name, last_name, describe_user, greet_user):
        self.first_name = first_name
        self.last_name = last_name
        self.describe_user = describe_user
        self.greet_user = greet_user

    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}.")
        print(f"Description: {self.describe_user}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
class Restaurant1:
    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restaurant {self.restaurant_name}.')
        print(f'The cuisine type is {self.cuisine_type}.')
        print(f'The location is {self.location}.')
        print(f'The price is {self.price_range}.')

    def can_you_take_a_date(self):
        if self.price_range > 20:
            print(f'''You can afford {self.restaurant_name}.''')
        else:
            print(f'''Don't embarrass yourself. It's too expensive!''')

class Restaurant2:
    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restaurant {self.restaurant_name}.')
        print(f'The cuisine type is {self.cuisine_type}.')
        print(f'The location is {self.location}.')
        print(f'The price is {self.price_range}.')

    def can_you_take_a_date(self):
        print(f'Checking if you can afford {self.restaurant_name}...')
        if self.price_range > 10000000:
            print(f'''You can afford {self.restaurant_name}.''')
        else:
            print(f'''Don't embarrass yourself. It's too expensive!''')

class Restaurant3:
    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restaurant {self.restaurant_name}.')
        print(f'The cuisine type is {self.cuisine_type}.')
        print(f'The location is {self.location}.')
        print(f'The price is {self.price_range}.')

    def can_you_take_a_date(self):
        if self.price_range > 10:
            print(f'''You can afford {self.restaurant_name}.''')
        else:
            print(f'''Don't embarrass yourself. It's too expensive!''')

chase_ace = Restaurant1("Chase's Aces", "Everything Good", "Dover, Delaware", int(input("Enter the price range: ")))
chase_ace.describe_restaurant()
chase_ace.can_you_take_a_date()

john_pizza = Restaurant2("U Can't Eat Me!", "Pizza", "Boston, Massachusetts", int(input("Enter the price range: ")))
john_pizza.describe_restaurant()
john_pizza.can_you_take_a_date()

kanes_bakery = Restaurant3("Hell's Bakery", "Baked Goods", "Knox County, Tennessee", int(input("Enter the price range: ")))
kanes_bakery.describe_restaurant()
kanes_bakery.can_you_take_a_date()
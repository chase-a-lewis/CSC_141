class Restaurant:
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
        if self.price_range > 40:
            print(f'''You can afford {self.restaurant_name}.''')
        else:
            print(f'''Don't embarrass yourself. It's too expensive!''')

chase_ace = Restaurant("Chase's Aces", "Everything Good", "Dover, Delaware", int(input("Enter the price range: ")))

chase_ace.describe_restaurant()
chase_ace.can_you_take_a_date()
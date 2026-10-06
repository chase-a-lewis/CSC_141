favorite_numbers = {
    "john": [7, 12],
    "chase": [6, 7, 67],
    "ligma": [69],
    "mark": [30, 40],
    "david": [3, 6, 9]
}

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)

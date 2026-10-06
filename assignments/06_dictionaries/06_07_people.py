person_1 = {
    "first_name": "Chase",
    "last_name": "Lewis",
    "age": 18,
    "city": "Felton"
}

person_2 = {
    "first_name": "Bruce",
    "last_name": "Wayne",
    "age": 30,
    "city": "Gotham"
}

person_3 = {
    "first_name": "Selina",
    "last_name": "Kyle",
    "age": 28,
    "city": "Gotham"
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nFirst name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
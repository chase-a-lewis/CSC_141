pet_1 = {
    "animal": "dog",
    "name": "Ace",
    "age": 4,
    "owner": "Terry"
}

pet_2 = {
    "animal": "cat",
    "name": "Selina",
    "age": 6,
    "owner": "Bruce"
}

pet_3 = {
    "animal": "dog",
    "name": "John Cena",
    "age": 7,
    "owner": "Luke"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nPet name: {pet['name']}")
    print(f"Animal: {pet['animal']}")
    print(f"Age: {pet['age']}")
    print(f"Owner: {pet['owner']}")
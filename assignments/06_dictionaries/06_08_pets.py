pet_1 = {
    "animal": "dog",
    "owner": "John"
}

pet_2 = {
    "animal": "cat",
    "owner": "Selina"
}

pet_3 = {
    "animal": "dog",
    "owner": "Bruce"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nAnimal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
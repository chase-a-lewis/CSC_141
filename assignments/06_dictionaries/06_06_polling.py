favorite_languages = {
    "selina": "spanish",
    "katheline": "japanese",
    "angelina": "chinese",
    "cassy": "german",
}

people_to_poll = [
    "selina",
    "katheline",
    "angelina",
    "cassy",
    "edward",
    "jacob"
]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")
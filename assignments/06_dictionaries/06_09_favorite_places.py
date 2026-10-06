favorite_places = {
    "john": ["New York", "Paris"],
    "jordan": ["London", "Tokyo", "Rome"],
    "mike": ["Miami"]
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")
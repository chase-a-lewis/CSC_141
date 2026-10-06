cities = {
    "new york": {
        "country": "United States",
        "population": "about 8 million",
        "fact": "Has the Statue of Liberty."
    },

    "london": {
        "country": "United Kingdom",
        "population": "about 9 million",
        "fact": "There is a cool clock named ben."
    },

    "tokyo": {
        "country": "Japan",
        "population": "about 14 million",
        "fact": "It is one of the world's largest cities."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
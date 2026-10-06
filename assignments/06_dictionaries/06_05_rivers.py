rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

# Print a sentence about each river.
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

# Print each river.
for river in rivers:
    print(river.title())

print()

# Print each country.
for country in rivers.values():
    print(country.title())
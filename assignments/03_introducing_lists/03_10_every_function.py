cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]

print(cities)

print(cities[0])

cities[1] = "Rome"
print(cities)

cities.append("Toronto")
print(cities)

cities.insert(2, "Berlin")
print(cities)

del cities[0]
print(cities)

cities.remove("Paris")
print(cities)

cities.sort()
print(cities)

cities.reverse()
print(cities)

print(len(cities))
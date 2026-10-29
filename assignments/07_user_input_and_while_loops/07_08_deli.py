sandwichs = ['peanut butter', 'jelly', 'evil', 'a little less evil', 'a little more evil', 'evilest']
finished_sandwiches = []

while sandwichs:
    current_sandwich = sandwichs.pop()
    print(f"I'm making a {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
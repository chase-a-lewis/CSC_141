
player_name = "Warrior"
health = 100
damage = 20
speed = 5

if health > 0:
    print("Warrior is alive!")
else:
    print("Warrior is dead!")

print("My 2D game is starting!")
print("Character:", player_name)
print("Health:", health)
print("Damage:", damage)
print("Speed:", speed)

# Current step: using a loop
for i in range(3):
    print("The game is running!")

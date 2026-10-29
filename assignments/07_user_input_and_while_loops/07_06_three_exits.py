topping = input("Enter a topping (or quit): ")

while topping != "quit":
    print(f"I'll add {topping} to your pizza.")
    topping = input("Enter a topping (or quit): ")

active = True

while active:
    topping = input("Enter a topping (or quit): ")

    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

while True:
    topping = input("Enter a topping (or quit): ")

    if topping == "quit":
        break

    print(f"I'll add {topping} to your pizza.")
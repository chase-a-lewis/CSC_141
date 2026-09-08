guests = ['Tyler', 'Ian', 'Moreghan', 'Demarion', 'Michael']

print(f"Hello {guests[0]}, you are invited to dinner!")
print(f"Hello {guests[1]}, you are invited to dinner!")
print(f"Hello {guests[2]}, you are invited to dinner!")
print(f"Hello {guests[3]}, you are invited to dinner!")
print(f"Hello {guests[4]}, you are invited to dinner!")

print("\nUnfortunately, " + guests[0] + " can't make it to dinner.\n")

guests[0] = 'Craig'
print(f"Hello {guests[0]}, you are invited to dinner!")
print(f"Hello {guests[1]}, you are invited to dinner!")
print(f"Hello {guests[2]}, you are invited to dinner!")
print(f"Hello {guests[3]}, you are invited to dinner!")
print(f"Hello {guests[4]}, you are invited to dinner!")

print("\nGood news! We found a bigger dinner table!\n")

guests.insert(0, 'Laniah')
guests.insert(2, 'Jared')
guests.append('Sami')

print(f"Hello {guests[0]}, you are invited to dinner!")
print(f"Hello {guests[1]}, you are invited to dinner!")
print(f"Hello {guests[2]}, you are invited to dinner!")
print(f"Hello {guests[3]}, you are invited to dinner!")
print(f"Hello {guests[4]}, you are invited to dinner!")
print(f"Hello {guests[5]}, you are invited to dinner!")
print(f"Hello {guests[6]}, you are invited to dinner!")
print(f"Hello {guests[7]}, you are invited to dinner!")

print("\nUnfortunately, we can only invite two people to dinner.\n")

print(f"Hello {guests.pop(7)}, you are no longer invited to dinner.")
print(f"Hello {guests.pop(6)}, you are no longer invited to dinner.")
print(f"Hello {guests.pop(5)}, you are no longer invited to dinner.")
print(f"Hello {guests.pop(4)}, you are no longer invited to dinner.")
print(f"Hello {guests.pop(3)}, you are no longer invited to dinner.")
print(f"Hello {guests.pop(2)}, you are no longer invited to dinner.")

print(f"\nHello {guests[0]}, you are still invited to dinner!")
print(f"Hello {guests[1]}, you are still invited to dinner!")

del guests[1]
del guests[0]

print(f"\nGuest list is now empty: {guests}")
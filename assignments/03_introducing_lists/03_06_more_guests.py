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
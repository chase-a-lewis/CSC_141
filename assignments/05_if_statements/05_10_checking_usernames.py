current_users = ["admin", "Jaden", "Sarah", "Mike", "Emily"]

new_users = ["John", "Sarah", "Alex", "JADEN", "Taylor"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} will need to enter a new username.")
    else:
        print(f"{new_user} is available.")

#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
#Make sure you use each character combination, "\t" and "\n", at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name = "    \tChase    "
last_name = "    \n\tLewis\n    "
print(name + last_name)
print(name.lstrip() + last_name.lstrip())
print(name.rstrip() + last_name.rstrip())
print(name.strip() + last_name.strip())
#Chase Lewis is the GOAT

#This program prints a name using variables and uses different thingys to do different things!
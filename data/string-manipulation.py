name = "Berkay Gediz"
print(name[1])

# Tab character
print("Berkay\tGediz")

# Newline character
print("Berkay\nGediz")

# Backslash
print("Berkay\\Gediz")

# Single quotes
print('Berkay Gediz')

# %s escape character
print("My name is %s" % name)

# %d escape character
age = 25
print("My age is %d" % age)

# f-string
print(f"My name is {name} and I'm {age} years old")

# format escape character
print("My name is {0} and I'm {1} years old".format(name, age))

# Convert to uppercase
name_upper = name.upper()
print(name_upper)

# Convert to lowercase
name_lower = name.lower()
print(name_lower)

# Strip operation
name_with_spaces = " Berkay Gediz "
print(name_with_spaces.strip())

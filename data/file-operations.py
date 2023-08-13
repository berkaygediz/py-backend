# Open the file for reading
F = open("/home/username/exampletext.txt", "r")
print(F.read())

# Read a single line
F.readline()

# Reset the file cursor to the beginning
F.seek(0)

# Close the file after reading
F.close()

# Open the file for appending
F = open("/home/username/exampletext.txt", "a")
F.write("Berkay\nGediz")

# Close the file after appending
F.close()

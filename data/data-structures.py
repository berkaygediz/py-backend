# Tuple definition
t = ("Berkay", "Gediz", 25, True)
print(t)
print(t[2:4])

# Sending multiple numerical parameters


def addition(*numbers):
    print(numbers)


addition(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Dictionary definition with a list of tuples
dictionary_list = [
    ("kitap", "book"),
    ("bilgisayar", "computer"),
    ("programlama", "programming")
]
print(dictionary_list[0][1])

# Dictionary definition with key-value pairs
fruits = {
    "elma": "apple",
    "armut": "pear",
    "muz": "banana"
}
print(fruits["elma"])

fruits["karpuz"] = "watermelon"
print(fruits)

del fruits["karpuz"]
print(fruits)

print(fruits.keys())
print(fruits.values())
print(fruits.items())
print(fruits.get("elma"))

fruits = []
print(type(fruits))

fruits.append("apple")
fruits.append("pear")
fruits.append("banana")
fruits.append("watermelon")

print(fruits[0])
print(fruits)

i = 2
print(fruits[i])
print(len(fruits))

fruit_count = len(fruits)
print(fruit_count)

print("For in:")
for fruit in fruits:
    print(fruit)

print("For i in:")
for i in range(5):
    print(i)

print("Remove the last element:", fruits.pop())

fruits.remove("pear")
print("Pear removed:", fruits)

apple_count = fruits.count("apple")
print("Number of apples:", apple_count)

apple_index = fruits.index("apple")
print("Index of apple:", apple_index)

fruits.reverse()
print("Reversed:", fruits)

fruits.sort()
print("Sorted:", fruits)

fruits.insert(0, "cantaloupe")
print("Insert cantaloupe:", fruits)

vegetables = ["potato", "beans", "tomato"]
print("Vegetables:", vegetables)

fruits.extend(vegetables)
print("Fruits and vegetables:", fruits)

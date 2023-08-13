# try except
try:
    sayi = int(input("Enter a number: "))
    print(sayi)
except ValueError:
    print("Please enter a valid number")

# try except else
try:
    sayi = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
else:
    print(sayi)

# try except finally
try:
    sayi = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
finally:
    print(sayi)
    print("Operation completed")

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero is not allowed"


def print_username(name):
    print("Username:", name)


def show_age(age):
    print("Age:", age)

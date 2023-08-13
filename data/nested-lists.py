cars = [
    [1, "BMW", 2010],
    [2, "Mercedes", 2015],
    [3, "Audi", 2018]
]

print("Cars:", cars)

print("Second element of cars:", cars[1])

print("Enter car product ID:")
car_id = int(input())

for car in cars:
    if car[0] == car_id:
        print("Car information:", car)

print("Object properties:", dir(cars))

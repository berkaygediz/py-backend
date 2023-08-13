print("Enter your weight (kg): ")
weight = int(input())
print("Enter your height (m): ")
height = float(input())

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight", bmi)
elif 18.5 <= bmi < 25:
    print("Normal weight", bmi)
elif 25 <= bmi < 30:
    print("Overweight", bmi)
elif 30 <= bmi < 40:
    print("Obese", bmi)
else:
    print("Severely obese", bmi)

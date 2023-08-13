from modules import math_functions_module

print("Enter two numbers to find their average and sum:")
print("Enter data 1:")
data1 = int(input())
print("Enter data 2:")
data2 = int(input())

avg = math_functions_module.average(data1, data2)
sum_result = math_functions_module.addition(data1, data2)

print("Average of the entered values:", avg)
print("Sum of the entered values:", sum_result)

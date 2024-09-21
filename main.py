import math
x = int(input("Введите x: "))
y = int(input("Введите y: "))
a = abs(x ** (y/x) - (math.sqrt(y / x) ** 3)) + (y - x)
print(a)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

sum = a + b
difference = a - b
product = a * b
average = (a + b) / 2
absolute_difference = max(abs(a), abs(b)) - min(abs(a), abs(b))

print("Сумма двух чисел:", sum)
print("Разность двух чисел:", difference)
print("Произведение двух чисел:", product)
print("Среднее арифметическое двух чисел:", average)
print("Разность максимального и минимального по модулю:", absolute_difference)
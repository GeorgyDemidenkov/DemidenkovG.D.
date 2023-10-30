#нахождение нод
def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#нахождение нок
def nok(a, b):
    return (a * b) // nod(a, b)
num1 = int(input("Введите первое натур число: "))
num2 = int(input("Введите второе натур число: "))

print("Нод:", nod(num1, num2))
print("Нок:", nok(num1, num2))

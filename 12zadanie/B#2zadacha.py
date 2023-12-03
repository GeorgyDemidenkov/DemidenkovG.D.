def find(numbers):
    if len(numbers)==0:
        return None
    max_num=max(numbers)
    numbers.remove(max_num)
    premax=max(numbers)
    return premax

numbers=[]

while True:
    num=int(input("Введите последовательность натуральных чисел по одному(0-конец): "))
    if num==0:
        break
    numbers.append(num)
premax=find(numbers)

print("Значение второго по величине элемента последовательности:", premax)

def sumcifr(n):
    if n < 10:
        return n
    else:
        return sumcifr(n % 10) + sumcifr(n // 10)

n = int(input("Введите число"))
print(sumcifr(n))

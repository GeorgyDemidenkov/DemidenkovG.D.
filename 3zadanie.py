#1
a=int(input("Введите числи а "))
b=int(input("Введите число b "))
c=int(input("Введите число c "))
print("Сумма", a+b+c)


#2
a=int(input("введите 1 катет-"))
b=int(input("введите 2 катет-"))
print("Площадь", 1/2*a*b)


#3
a=int(input("введите количество минут с начала суток"))
print("Время", (a//60)%24, a%60)


def abc(a,b,l,N):
    print(2*N+(2*l-1)*a+2*(l-1)*b)
#4
a=int(input("введите расстояние между рядами"))
b=int(input("введите расстояние между дырочками"))
l=int(input("введите длина конца шнурка"))
N=int(input("введите количество дырочек"))
abc(a,b,l,N)


def aaa(a,b,c):
    if a<b and a<c:
        d=a
    elif b<c and b<a:
        d=b
    else:
        d=c
    return d
#5
a=int(input("введите первое число"))
b=int(input("введите второе "))
c=int(input("введите третье"))
d=aaa(a,b,c)
print("Наименьшее", d)


def bbb(a,b,c,d):
    e=(a+b)%2
    f=(c+d)%2
    if e+f==0:
        print("да")
    else:
        print("нет")
#6
a=int(input("введите строку 1"))
b=int(input("введите столбец 1"))
c=int(input("введите строку 2"))
d=int(input("введите столбец 2"))
bbb(a,b,c,d)


def ccc(a):
    if a%4==0 and a%100!=0:
        print("да")
    elif a%400==0:
        print("да")
    else:
        print("нет")
#7
a=int(input("введите год"))
ccc(a)


def ddd(a,b,c):
    if a==b and b==c:
        print(3)
    elif a==b or b==c or a==c:
        print(2)
    else:
        print(0)
#8
a=int(input("введите первое число"))
b=int(input("введите второе "))
c=int(input("введите третье"))
ddd(a,b,c)


def eee(a,b,c):
    if a*b>c and c%a==0:
        print("да")
    elif a*b>c and c%b==0:
        print("да")
    else:
        print("нет")
#9
a=int(input("введите первое число"))
b=int(input("введите второе "))
c=int(input("введите третье"))
eee(a,b,c)

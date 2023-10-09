def aaa(a,b):
    while a<=b:
        print(a)
        a=a+1

a=int(input())#1
b=int(input())
aaa(a,b)

def bbb(a,b):
    if a<b:
        while a<=b:
            print(a)
            a=a+1
    else:
        while b<=a:
            print(a)
            a=a-1
a=int(input())#2
b=int(input())
bbb(a,b)


def ccc(a,b):
    while a>=b:
        if a%2!=0:
            print(a)
        a=a-1
a=int(input())#3
b=int(input())
ccc(a,b)


def ddd(n,b):
    while n>0:
        print("введите число №",n)
        a=int(input())
        b=b+a
        n=n-1
    print(b)
#4
n=int(input("введите кол-во n"))
b=0
ddd(n,b)



def eee(n,b):
    while n>0:
        a=n**3
        b=b+a
        n=n-1
    print(b)
#5
n=int(input("введите число n"))
b=0
eee(n,b)


def fff(n,b):
    while n>0:
        b=b*n
        n=n-1
    print(b)
#6
n=int(input("введите число n"))
b=1
fff(n,b)


def ggg(n,b,c,v):
    while v<=n:
        b=b*v
        c=b+c
        v=v+1
    print(c)
#7
n=int(input("введите число n"))
b=1
c=0
v=1
ggg(n,b,c,v)


def hhh(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j,end="")
        print()
n = int(input())#8
hhh(n)


def iii(a,b,n,c,e):
    while c<n-2:
        d=a+b
        a=b
        b=d
        c=c+1
        e=e+b
    print("Сумма",e)
a=1#9
b=1
n=int(input("введите N"))
c=0
e=2
iii(a,b,n,c,e)

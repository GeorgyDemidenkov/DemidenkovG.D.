def farq(n):
    a=1
    b=0
    while a*2<=n:
        a*=2
        b+=1
    print(a, b)
n=int(input())
farq(n)

#var6
mas=[]#1
 
for value in range(10):
    value=int(input("Введите элемент массива: "))
    mas.append(value)
 
element=max(mas)
print("Наибольший элемент массива:",element)
 
b=0
m=0
for i in mas:
    if i>element:
        b=b+1
    elif i<element:
        m=m+1
print("элементов >",b)
print("элементов <",m)
mas.clear()

mas=[]#2
s=0
for i in range(10) :
    mas.append(int(input()))
    if mas[-1]>5 :
        s=s+mas[-1]
print(s)

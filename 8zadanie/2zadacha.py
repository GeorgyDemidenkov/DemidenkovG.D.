import math
def s(p1, p2):
    a=math.sqrt(p1*(p1-ab)*(p1-bc)*(p1-ac)) + math.sqrt(p2*(p2-ad)*(p2-cd)*(p2-ac))
    return a
ab=int (input("Введите длину стороны AB"))
bc=int (input("Введите длину стороны BC"))
cd=int (input("Введите длину стороны CD"))
ad=int (input("Введите длину стороны AD"))
ac=int (input("Введите длину стороны AC"))
p1=(ab + bc + ac) // 2
p2=(ad + cd + ac) // 2
print(s(p1, p2))

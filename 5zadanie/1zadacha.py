def kef(A,B):
  if A<=B:
  for i in range(A,B+1):
    print(i)
  else:
    print("A нужно < или = B")
A=int(input()) 
B=int(input()) 
kef(A,B)

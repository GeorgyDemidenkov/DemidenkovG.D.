def farq(n):
  c=0
  l=0
  while True:
    if n==0:
      break
    l+=n
    c+=1
    print(l/c)
n=int(input())
farq(n)

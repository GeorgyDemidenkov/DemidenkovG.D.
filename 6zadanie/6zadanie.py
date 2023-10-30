def dfg(string):
  string = string.replace("a", "")
  return string
def dfgd(string):
  count = len(string) - len(string.replace("a", ""))
  return count
string=input("введите строку")
count= dfgd(string)
string= dfg(string)
print(string)
print(str(count))

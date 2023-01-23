s = input("Enter a string:")
dOut = {}
def StringtoDict(string):
    count = 0
    lst = list(string)
    for i in lst:
      if i not in dOut and lst.count(i)==1:
        count = 1
        dOut.update({i:count})
      else:
        while lst.count(i)>1:
            count = count+1
            lst.remove(i)
            dOut.update({i:count})
      count = 1

    print(dOut)
StringtoDict(s)

myDict1 = {'a':1,'e':7,'f':4,'b':3}
myDict2 = {'b':10,'c':9,'d':5,'a':8}
sDict = {}
def SumDicts(dict1,dict2):
    for i in dict1:
        if i in dict2:
           sDict[i] = dict1[i]+dict2[i]
    print(sDict)
SumDicts(myDict1,myDict2)


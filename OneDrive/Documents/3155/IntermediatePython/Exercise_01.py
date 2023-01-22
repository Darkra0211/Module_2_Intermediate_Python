myList = [1,1,1,2,3,3,3,3,4,5,6]

def Get_unique_List(list):
   lst = list
   unique_List = []
   for i in lst:
        if i not in unique_List:
            unique_List.append(i)
      
   print(unique_List)
Get_unique_List(myList)

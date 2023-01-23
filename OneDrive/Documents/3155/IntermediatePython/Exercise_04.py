def sumList():
    sList = []
    sum = 0
    for i in range(0,5):
       num = input("Enter int #" + (str)(i+1) +":")
       if num.isdigit():
           sum = sum+ int(num)   
       else:
            while not num.isdigit():
                num = input("Invalid input. Please enter an int.")
            if num.isdigit():
                sum = sum+int(num)

    print("Your sum is " + str(sum))
sumList()




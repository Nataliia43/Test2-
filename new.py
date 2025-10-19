try:
    x = int(input("Input the first number"))
    y = int(input("INput the second number "))
    list = []
    list.append(x)
    list.append(y)
    count =0
    while count>6 :
        count +1
        z= x+y
        list.append[z]
        x= y 
        y =z
        print(list)


except Exception as e:
    print("An error occurred:", e)
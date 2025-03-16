num1=float(input("enter num1:"))#the user enters number 1
operation=input("enter anyoperation like +,- etc:")
num2 =float(input("enter num2:"))#the user enters number 2
if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("invalid operation")

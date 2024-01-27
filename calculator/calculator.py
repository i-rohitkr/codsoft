def add (x,y):
    return x+y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division (x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y
        

while True:
    print("\nChoose operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Divison")
    print("5.Exit")

    choice = input("Enter choice(1/2/3/4):")
    if choice in ("1","2","3","4","5"):
        num1 = float(input("enter the first number:"))
        num2 = float(input("enter the second number:"))

        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == "2":
            print(num1,"-",num2,"=",subtraction(num1,num2))
        elif choice == "3":
            print(num1,"*",
                  num2,"=",multiplication(num1,num2))
        elif choice =="4":
            print(num1,"/",num2,division(num1,num2))
        else:
            print("Exiting Calculator....")
            break
    else:
        print("Invalid input")    

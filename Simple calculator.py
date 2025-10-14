#Calculator
def calculator():
    while True:
        z=str(input("Do you want to use calculator? (y/n): "))
        if z=="y":
            x=float(input("Enter first number: "))
            y=float(input("Enter second number: "))
            op=str(input("Enter operation (+, -, *, /, //, %, **): "))
            if op=="+":
                print(f"{x} + {y} = {x+y}")
            elif op=="-":
                print(f"{x} - {y} = {x-y}")
            elif op=="*":
                print(f"{x}*{y} = {x*y}")
            elif op=="/":
                if y==0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"{x}/{y} = {x/y}")
            elif op=="//":
                if y==0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"{x}//{y} = {x//y}")
            elif op=="%":
                if y==0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"{x}%{y} = {x%y}")
            elif op=="**":
                print(f"{x}**{y} = {x**y}")
            else:
                print("Invalid operation. Please try again.")
        elif z=="n":
            print("Exiting calculator. Goodbye!")
            break
calculator()

    

    
    



import sys
import math
print("Area Calc.")
print("Choose:\n1)Triangle\n2)Circle\n3)Rectangle\n4)Square\n5)Quit")
ch=int(input("Enter your choice: "))
if ch==1:
    a = int(input("Enter the base of triangle: "))
    b = int(input("Enter the height of triangle: "))
    area_T=(a*b)*(1/2)
    print("Area of the triangle is ",area_T)
    sys.exit()
elif ch==2:
    r=int(input("Enter the radius of Circle:"))
    area_C=math.pi*(r**2)
    print("Area of the circle is ",area_C)
    sys.exit()
elif ch==3:
    x=int(input("Enter the length of Rectangle:"))
    y=int(input("Enter the breadth of Rectangle:"))
    area_R=x*y
    print(f"Area of the rectangle is {area_R}")
    sys.exit()
elif ch==4:
    s=int(input("Enter the length of Square:"))
    area_S=s*s
    print("Area of the square is ",area_S)
    sys.exit()
elif ch==5:
    print("Goodbye!")
    sys.exit()
else:
    print("Error: Invalid Input. Run the code again.")
    sys.exit()

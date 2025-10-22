# Write code below 💖

print("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk")

x = int(input("Enter ur answer:"))

print("Q2) Which kind of instrument most pleases your ear?:\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum")

y = int(input("Enter ur answer:"))

print("Q3) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")

z = int(input("Enter ur answer:"))
s = 0
g = 0
r = 0
h = 0

if x == 1:
    g = +1
    r = +1
elif x == 2:
    s = +1
    h = +1
else:
    print("Invalid Input. Run the program again.")

if z == 1:
    h = +2
elif z == 2:
    s = +2
elif z == 3:
    r = +2
elif z == 4:
    g = +2
else:
    print("Invalid Input. Run the program again.")

if y == 1:
    s = +4
elif y == 2:
    h = +4
elif y == 3:
    r = +4
elif y == 4:
    g = +4
else:
    print("Invalid Input. Run the program again.")

print(f"Slytherin:{s} Hufflepuff:{h} Ravenclaw:{r} Gryffindor:{g}")

if s > g and s > r and s > h:
    print("You belong to Slytherin.")
elif h > s and h > r and h > g:
    print("You belong to Hufflepuff.")
elif g > s and g > h and g > r:
    print("You belong to Gryffindor.")
elif r > s and r > g and r > h:
    print("You belong to Ravenclaw.")
else:
    print("Error. Run the code again.")



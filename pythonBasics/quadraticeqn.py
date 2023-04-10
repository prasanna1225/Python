#Python Program to Solve Quadratic Equation


import math

a = int(input("enter a num :"))
b = int(input("enter a num :"))
c = int(input("enter a num :"))

d = (b**2) - (4*a*c)

sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
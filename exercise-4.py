# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle



x = input("please enter the measurments for side 1 of the tirangle")
y = input("please enter the measurments for side 2 of the tirangle")
z = input("please enter the measurments for side 3 of the tirangle")

print("Input the sides of the triangle")

x= int(input("x:"))
y= int(input("y:"))
z= int(input("z:"))

if x == y == z:
    print("The triangle with sides of "+ x + y  + z  " is an Equilateral Triangle")
elif x==y or y==z or z==x:
    print("The triangle with sides of "+ x + y  + z  " is an Iscsceles Triangle")
else:
    print("The triangle with sides of "+ x + y  + z " is a Scalene Traingle")

# MATH OPERATER CONCEPTS: +, -, *, /, //, %, **

add = 7 + 2
print("Sum: ", add)

subtract = 7 - 2
print("Difference: ", subtract)

multiply = 7 * 2
print("Product: ", multiply)

float_divide = 7 / 2
print("Float Quotient: ", float_divide)

integer_divide = 7 // 2
print("Integer Quotient: ", integer_divide)

modulus = 7 % 2
print("Remainder: ", modulus)

exponent = 7 ** 2
print("Exponent: ", exponent)

print(2 + 2 != 10 - 6) # conditionals


# Order of Operation

result1 = (2 + 3) * 4
print("Result 1: ", result1)

result2 = 2 ** 3 * 4
print("Result 2: ", result2)

result3 = 20 / 5 * 2
print("Result 3: ", result3)

result4 = 10 - 2 + 3
print("Result 4: ", result4)

result5 = 5 + 2 ** 3 * (4 - 3)
print("Result 5: ", result5)

# CHALLENGES

# Challenge 1
# Calc. Area of Rectangle
# width 8 an hieght 5

Width = 8
Hieght = 5
print("Area of Rectangle: ", Width * Hieght)

# Challenge 2
# Use the form. pir^2 to calc area of circle with raduis as 7
# ( pi as 3.14)

pi = 3.14
radius = 7
print("Area of Cirlce: ", pi * radius ** 2)

# Challege 3
# A book is 12.99 and notebook is 3.50
# Find tatal cost of 3 books and 4 notebooks

book = 12.99
notebook = 3.50
print("Total Cost: ", book *  3 + notebook * 4)

# Challenge 4 
# create an integer variable
# use modulus to check if even or odd
# explain resoning

num = 7

if num%2 == 0:
    print("Even")
else:
    print("Odd")



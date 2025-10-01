# Python libraries are collections of pre-written code that you can import and use in your own programs.
# Doc on libraries: https://docs.python.org/3/library/index.html

#Key concepts: libraries, import math, import random

#------------------
# MATH LIBRARY
#------------------

# Doc on Math library: https://docs.python.org/3/library/math.html

import math

print("Square Root: ", math.sqrt(25))
print("Round Up to an Integer: ", math.ceil(3.4))
print("Round Down to an Integer: ", math.floor(6.8))
print("Power: ", math.pow(2, 5))
print("Pi", math.pi)

# Pseudorandom Nnumber Generators (PRNG) vs True random numbers (TRNG). 
# Watch Tom Scott video on lava lamps and randomness: https://www.youtube.com/watch?v=1cUUfMeOijg
# Optional video: Computerphile Random Numbers with LFSR (Linear Feedback Shift Register): https://www.youtube.com/watch?v=Ks1pw1X22y4


# ** PRECURSER CHALLENGE **
# Create your own Pseudorandom Number Generator (PRNG) that utilizes a seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float DOWN to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10.

import random 

seed = 798.0982
seed /= 4.9
seed -= 279.023
seed *= 97.0932
print(seed)
seed = math.floor(seed)
seed = seed % 10
print(seed)

print(random.randint(1, 100))
print(random.random())

mylist = ["cero", "cheez", "pollo"]
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

radius = 14/2
circle_area = math.pi * radius ** 2
print(circle_area)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

Die_Result = random.randint(1, 6)
print(Die_Result)

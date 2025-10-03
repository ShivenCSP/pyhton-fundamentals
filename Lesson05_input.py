# USER INPUT IN PYTHON

# print("\n--- User Input Demonstration ---")

# name = input("Enter your name: ")
# print("Hello,", name)

# age = input("Enter your age: ")
# print(f"You are {age} years old.")
# print(type(age))

# age_number = int(age)
# print(f"Next year, you will be: {age_number + 1} years old")
# print(type(age_number))

# # Example with float input
# height = float(input("Enter your height in meters: "))
# print(f"You are {height} meters tall.")

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

Color = input("What is your favorite color: ")
print(f"Your favorite color is {Color}.")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

num1 = float(input("What is your first number: "))
num2 = float(input("What is your second number: "))
print(f"Your sum is {num1 + num2}.")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

import math

diameter = float(input("What is your diameter: "))
radius = diameter/2
area = math.pi * radius ** 2

print(f"The area of your circle is: {area}")

# Challenge: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random

side = int(input("How many sides should there be on the die: "))
print(f"Result: {random.randint(1, side)}")
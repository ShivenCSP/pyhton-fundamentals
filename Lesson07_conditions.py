# # CONDITIONALS IN PYTHON
# # comparison operators: ==, !=, <, >, <=, >=
# # logical operators: and, or, not
# # control flow: if, elif, else

# print()
# print("--- Conditionals in Python ---")

# print( 3 ==2 )   
# print("Hello" == "Hi there")
# print( 7 != 4)
# print(4 > 5)

# print()
# print()
# print()
# print()

# # if
# num1 = 12
# if num1 == 10: 
#     print("Your number is equal to 10")

# num2 = 5
# print(num2 <= 12)
# if num2 <= 12:
#     print("Your number is less than or equal to 12")
# else: 
#     print("Your number is greater than 12")

# #if elif else

# temperature = 72
# if temperature > 80: 
#     print("It's hot!")
# elif temperature >= 60:
#     print("It's nice.")
# else:
#     print("It's cold!")

# print()
# print("--- Comparing Values with if/elif/else ---")

# x = 20
# y = 20

# if x == y: 
#     print("x is equal to y")
# elif x > y:
#     print("x is greater than y")
# elif x < y: 
#     print("x is less than y")
# else: 
#     print("error")

# # Logical operator: and
# # Both sides of the 'and' must  be true, otherwise it's false. 

# print()
# print()
# print() 

# age = 17
# has_permission = True

# if age >= 17 and has_permission:
#     print("You can drive")
# else:
#     print("Can't drive yet")

# # Using 'or' and 'not'
# print("--- Using 'or' --- ")
# day = "3e,3oindienwndwnfnwodn"

# if day == "Saturday" or  day == "Sunday":
#     print("It's the weekend!:)")
# elif day == "Monday" or day == "Tuesday" or day == "Wednsday" or day == "Thursday" or day == "Friday":
#     print("Its the Weekday...:(")
# else:
#     print("Beep, Beep, Beeepe, Invalid. Program Crashing!!! Beeeep!")

# # Challenge 1: Even or Odd
# # Ask the user for a number, and tell them if it’s even or odd.
# # Example output:
# # Enter a number: 7
# # 7 is odd.
# # Hint: use modulus operator

num = int(input("What is a number: "))

if num % 2 == 0:
     print("Your number is Even")
else:
     print("Your number is Odd")

# Challenge 2: Password Check
# Create a variable with a stored password
# Ask the user to enter a password. 
# If it matches the stored password, print "Access granted." Otherwise, "Access denied."
# Example output:
# Enter password: dolphin
# Access granted. Access denied.
# Enter password: swordfish
# Access granted.

password = "gipkit213"
user_try = input("What is the password? - ")

if password == user_try:
     print("Access Granted")
else:
     print("Access Denied")

# Challenge 3: Grading System
# Ask the user for a numeric grade (0-100) and print a letter grade.
# Example output:
# Enter your grade: 94
# You earned an A.

num_grade = int(input("What is your numberical grade? - "))

if num_grade >= 90:
     print("Your grade is an A!!")
elif num_grade >= 80:
     print("Your grade is a B!")
elif num_grade >= 70:
     print("Your grade is a C")
elif num_grade >= 60:
     print("Your grade is a D")
elif num_grade <= 60:
     print("Your grade is a F")
else:
     print("Invalid Statment please run program again.")


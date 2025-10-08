# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o

# 0 1 2
# A d a

second_letter = greeting[1]
print(second_letter)

message = greeting + " " + name + "!!!!"
print("Concatenated message:", message)

word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last Letter:", word[-1])
print("Range of letters (non-inclusive):", word[3:7])
print("Range of letters (non-inclusive):", word[1:-7])
print(word[:5])
print("Last seven Letters:", word[-7:])
print("Step through every second character:", word[::-3])

## Built in functions

country = "idiotland64"
length_of_word = len(country)
print(length_of_word)

character = "spOnGeBOb SquARePaNTs"
print("Uppercase:", character.upper())
print("Lowercase:", character.lower())
print("Show:", character.capitalize())
print("Title:", character.title())

# DAY 2 OF STRINGS
# Find and replace text

sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
next_sentence = sentence.replace("goofy", "goober")
print(sentence)
print(new_sentence)
print(next_sentence)

name = "Shiven"
age = 16
city = "Whitehouse Station"

print(f"Hello, my name is {name}, I am {age} years old and live in {city}.")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}")

# CHALLENGES

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

print(len(input("What is your favorite quote: ")))

# Challenge 2: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
message = last_name + ", " + first_name
print("Concatenated Language:", message)

# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP

word = input("What is your word:")
print("Uppercase:", word.upper())
print("Lowercas:", word.lower())
print("Backwards:", word[::-1])




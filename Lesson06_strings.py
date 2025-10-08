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


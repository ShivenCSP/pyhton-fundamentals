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

phrase = "spOnGeBOb"
print("Uppercase:", phrase.upper())
print("Lowercase:", phrase.lower())
print("Show:", phrase.capitalize())



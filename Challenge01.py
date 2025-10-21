# Challenges
# Challenge 1 - Palindrome checker

palindrome = "racecar"
if palindrome[-1::-1] == palindrome :
    print(True)
else:
    print(False)

# challenge 2
# Domain finder

email = input("What is your email: ")
at_symbol = email.find("@")
domain = email[at_symbol + 1::]
print("Here is your domain:", domain)

# Challenge 3
# List confirmer

my_list = ["bagel", "pancakes", "waffles", "french toast"]
last = my_list[-1]
user_food = input("Gimmie a breakfast food: ")

if last == user_food:
    print(True)
else:
    print(False)

# Challenge 4
# suffix adder

user_word = input("Gimmie a random word: ")
length = len(user_word)

if user_word[-3::] == "ing":
    print(user_word + "ly")
elif length <= 3:
    print(user_word)
elif length >= 3:
    print(user_word + "ing")
else:
    print("invalid string...")



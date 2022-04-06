import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "(){}[],./?';:\|-_*&^%$#@!~`+ "

# set true of false to use or not to use a character group in the password
upper, lower, nums, syms = False, False, True, True
all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += numbers

if syms:
    all += symbols

    # length of password
length = 5
    # number of passwords
amount = 1

for item in range(amount):
    password = "".join(random.sample(all, length)) # .sample() prevents reuse of characters in each password generated
    print("New password is ",password)
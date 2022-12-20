#!/usr/bin/python3
import random
from random import shuffle
print("\nPassword Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

# User input password length specifics
lettrs = int(input("\nHow many letters would you like? "))

numbs = int(input("\nHow many numbers would you like? "))

syms = int(input("\nHow many symbols would you like? "))

length = lettrs+numbs+syms

# print(letters[0])
# print(len(letters))

# generate user selected number of random letters
for lett in range(1, lettrs+1):
    randnum = random.randint(0, len(letters)-1)
    # print(randnum)
    password = password+(letters[randnum])

# print(password)

# generate user selected number of random numbers
for numb in range(1, numbs+1):
    randnum = random.randint(0, len(numbers)-1)
    #print(randnum, len(numbers))
    password = password+(numbers[randnum])

# print(password)

# generate user selected number of random symbols
for sym in range(1, syms+1):
    randnum = random.randint(0, len(symbols)-1)
    #print(randnum, len(numbers))
    password = password+(symbols[randnum])
print("")
print(f"Your password string is:\n{password}\n")

# Randomize the created pasword string
newpass = random.sample(password, len(password))
# print(newpass)

randpass = ""
for word in newpass:
    randpass = randpass+word
 # print(word)

print(f"Your randomized password is:\n{randpass}\n")

# additional way to randomize password
pass_list = list(password)
random.shuffle(pass_list)
print(pass_list)
#passwd = ""
# for paswd in pass_list:
#   newpass = newpass+paswd

# print(passwd)

import secrets
import string

letter = string.ascii_lowercase + string.ascii_uppercase
number = string.digits
symbol = string.punctuation

print("Welcome to Password generator")
length = int(input("What length do you want your password to be?"))
letters = int(input("How many letters do you want in your password?"))
numbers = int(input("How many numbers do you want in your password?"))
symbols = int(input("How many symbols do you want in your password?"))

key = []
key += [secrets.choice(letter) for _ in range(letters)]
key += [secrets.choice(number) for _ in range(numbers)]
key += [secrets.choice(symbol) for _ in range(symbols)]

password = ""

for i in range(length):
    password += secrets.choice(key)

print(password)

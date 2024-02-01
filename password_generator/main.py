import random
import string

plen = int(input("enter the length of password:"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
sym = string.punctuation

all = lower + upper + digits + sym

temp = random.sample(all, plen)

password = "".join(temp)

print("your password is :", password)
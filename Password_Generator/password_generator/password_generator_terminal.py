import random
import string
from colorama import Fore

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
hex = string.hexdigits
passw = ''
chars = 12

while len(passw) < chars:
    passw += random.choice(letters + digits + hex + punctuation)

print(f'\n{Fore.WHITE}Password: {Fore.GREEN}{passw}\n')
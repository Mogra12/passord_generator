from password_strength import PasswordPolicy
from password_strength import PasswordStats

policy = PasswordPolicy.from_names(
    length=12,
    uppercase=3,
    numbers=3,
    special=3,
    nonletters=3
)

password = input('Passord: ')
stats = PasswordStats(password)

if stats.strength() >= 0.66:
    print('Strong password')
elif stats.strength() >= 0.50 and stats.strength < 0.66:
    print('Medium password')
elif stats.strength() < 0.50:
    print('Weak password')

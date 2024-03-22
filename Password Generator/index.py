import string
import random

# Function to generate a random password
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Generate a list of characters to choose from
    chars = list(string.ascii_lowercase)

    if use_uppercase:
        chars.extend(list(string.ascii_uppercase))
    if use_numbers:
        chars.extend(list(string.digits))
    if use_special_chars:
        chars.extend(list(string.punctuation))

    # Generate a random password
    password = ''.join(random.choice(chars) for i in range(length))

    return password

# Prompt the user to specify the length and complexity of the password
length = int(input("Enter the desired length of the password: "))
use_uppercase = bool(input("Use uppercase letters? (y/n) ").lower().startswith('y'))
use_numbers = bool(input("Use numbers? (y/n) ").lower().startswith('y'))
use_special_chars = bool(input("Use special characters? (y/n) ").lower().startswith('y'))

# Generate a password using the specified parameters
password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

# Print the generated password
print("Generated password: ", password)

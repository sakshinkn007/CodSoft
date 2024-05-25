import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define the character sets to use
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining characters with a mix of all sets
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to avoid any predictable pattern
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

# Example usage:
if __name__ == "__main__":
    try:
        length = int(input("Enter the password length: "))
        print("Generated password:", generate_password(length))
    except ValueError as e:
        print(e)

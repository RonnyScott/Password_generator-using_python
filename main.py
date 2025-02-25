import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """
    Generates a secure password.

    :param length: Length of the password (default: 12)
    :param use_digits: Whether to include digits (default: True)
    :param use_special_chars: Whether to include special characters (default: True)
    :return: Generated password as a string
    """
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_digits, use_special_chars)
    print("Generated Password:", password)

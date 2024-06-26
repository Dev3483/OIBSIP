import random
import string

try:
     length = int(input("Enter the desired password length: "))
     include_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
     include_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
     include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
     include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
     password=""
     characters = ""
     if include_upper:
        characters += string.ascii_uppercase
     if include_lower:
         characters += string.ascii_lowercase
     if include_digits:
        characters += string.digits
     if include_special:
        characters += string.punctuation
     if len(characters) == 0:
        raise ValueError("No character types selected, cannot generate password.")

     password = ''.join(random.choice(characters) for i in range(length))
     print(f"Generated password: {password}")
except ValueError as e:
        print(f"Error: {e}")



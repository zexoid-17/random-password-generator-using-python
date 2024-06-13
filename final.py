import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected. Please choose at least one character type.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    # Ask the user for the number of passwords
    num_passwords = int(input("Enter the number of passwords you want to generate: "))
    
    # Ask the user for the password length
    password_length = int(input("Enter the desired password length: "))

    # Ask the user for character set preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and print the passwords
    try:
        for _ in range(num_passwords):
            password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_symbols)
            print("Generated password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

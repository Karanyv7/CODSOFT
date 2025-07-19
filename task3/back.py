import string
import random

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input(prompt):
    return input(prompt).strip().lower() in ['y', 'yes']

def main():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            raise ValueError

        use_upper = get_user_input("Include uppercase letters? (y/n): ")
        use_lower = get_user_input("Include lowercase letters? (y/n): ")
        use_digits = get_user_input("Include numbers? (y/n): ")
        use_symbols = get_user_input("Include special characters? (y/n): ")

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\n✅ Generated Password:\n{password}")

    except ValueError:
        print("❌ Invalid input. Please enter a positive number for length.")

if __name__ == "__main__":
    main()

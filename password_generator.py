import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4 characters."

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def password_generator():
    print("🔐 Secure Password Generator")
    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            print(f"Generated Password: {generate_password(length)}")
        except ValueError:
            print("Please enter a valid number.")
            continue

        again = input("Generate another password? (y/n): ").lower()
        if again != 'y':
            print("👋 Stay safe!")
            break

if __name__ == "__main__":
    password_generator()

import base64
import os

VAULT_FILE = 'vault.txt'

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper()for c in password)
    has_digit = any(c.isdigit()for c in password)
    has_special = any(c in "!@#$%^&*()_<>.," for c in password)

    score = sum([length >=8, has_upper, has_digit, has_special])
    return ["Weak", "Moderate", "Strong", "Very Strong"][min(score, 3)]

def add_credential():
    website = input("Enter website: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as f:
        f.write(encoded_line + '\n')

    print(f"Credential added. Password strength: {strength}")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials stored.")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded =  decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = '*' * len(password)
            print(f"Website: {website} | Username: {username} |Password: {password}")


def main():
    while True:
        print("\nCredential Manager")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "3": break
            case _: print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
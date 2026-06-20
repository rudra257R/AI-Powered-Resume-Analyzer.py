import re

def check_password_strength(password):

    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1

    # Special character check
    if re.search(r"[@#$%^&*!]", password):
        strength += 1

    # Result
    if strength == 5:
        return "Very Strong Password"
    elif strength >= 3:
        return "Medium Password"
    else:
        return "Weak Password"

# User input
wifi_password = input("Enter Wi-Fi Password: ")

# Check strength
result = check_password_strength(wifi_password)

print("\nPassword Strength:", result)
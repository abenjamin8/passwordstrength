
# Author: Adam Benjamin (https://github.com/abenjamin8)
# Project: password-strength-checker

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Final rating
    if score >= 6:
        strength = "Strong"
        colour = GREEN
    elif score >= 4:
        strength = "Medium"
        colour = YELLOW
    else:
        strength = "Weak"
        colour = RED

    return strength, feedback, colour


# Example usage
password = input("Enter a password to check: ")
strength, feedback, colour = check_password_strength(password)

print(colour + f"\nPassword Strength: {strength}" + RESET)
if feedback:
    print("Suggestions:")
    for f in feedback:
        print(" -", f)
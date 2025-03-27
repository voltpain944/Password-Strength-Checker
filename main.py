# Password-Strength-Checker
import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength[score]

password = input("Enter your password: ")
print(f"Password Strength: {check_password_strength(password)}")

#1stweek mini project 
import re
def check_password_strength(password):
    score = 0
    length_error = len(password) < 8
# Criteria checks using regular expressions
    lowercase = re.search(r"[a-z]", password)
    uppercase = re.search(r"[A-Z]", password)
    digit = re.search(r"\d", password)
    special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
# Scoring logic
    if not length_error:
        score += 1
    if lowercase:
        score += 1
    if uppercase:
        score += 1
    if digit:
        score += 1
    if special_char:
        score += 1
# Determine strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    return strength
# Example usage:
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")


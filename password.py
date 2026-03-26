import random
import string
def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
 """
 Password generate karta hai with custom options
 """
 characters = ""

 if use_letters:
    characters += string.ascii_letters
 if use_digits:
    characters += string.digits
 if use_symbols:
    characters += string.punctuation

 if not characters:
    return "Error: At least one character type required!"

 password = ""
 for i in range(length):
     password += random.choice(characters)

 return password
def check_password_strength(password):
 """
 Password ki strength check karta hai
 """
 strength = 0

 if any(c.islower() for c in password):
    strength += 1
 if any(c.isupper() for c in password):
    strength += 1
 if any(c.isdigit() for c in password):
    strength += 1
 if any(c in string.punctuation for c in password):
    strength += 1
 if len(password) >= 12:
    strength += 1

 if strength >= 4:
    return "Strong 🔐"
 elif strength >= 3:
      return "Medium 🔓"
 else:
     return "Weak ⚠️"
# ========== MAIN PROGRAM ==========
print("="*50)
print(" 🔐 ADVANCED PASSWORD GENERATOR 🔐")
print("="*50)
# Input: Password length
while True:
 try:
    length = int(input("\nEnter password length (8-50): "))
    if 8 <= length <= 50:
       break
    else:
       print("Please enter a number between 8 and 50.")
 except ValueError:
    print("Invalid input! Please enter a number.")
# Input: Character types
print("\nChoose character types to include:")
use_letters = input("Include letters (a-z, A-Z)? (y/n): ").lower() == 'y'
use_digits = input("Include numbers (0-9)? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols (!@#$...)? (y/n): ").lower() == 'y'
# Input: Kitne passwords chahiye
num_passwords = int(input("\nHow many passwords to generate? (1-10): "))
if num_passwords < 1:
   num_passwords = 1
elif num_passwords > 10:
   num_passwords = 10
# Generate passwords
print("\n" + "="*50)
print(" GENERATED PASSWORDS")
print("="*50)
for i in range(num_passwords):
    password = generate_password(length, use_letters, use_digits, use_symbols)
    strength = check_password_strength(password)

    print(f"\n{i+1}. {password}")
    print(f" Strength: {strength}")
print("\n" + "="*50)
print("✅ Password generation complete!")

# Initialize
correct_password = "ADMIN"
attempts = 0

# Indefinite loop
while True:
    user_input = input("Type password to unlock: ")
    attempts += 1
    if user_input == correct_password:
        print("Unlocked.")
        break
    else:
        print("Access Denied")

# Output assessment
print(f"Input Attempts: {attempts}")
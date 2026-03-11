# %%
# Exercise 2 – Deterministic Forensic Hash

# Initialize variables
ENGINEER = "LIM"          # Your engineer name
SEED_NUM = 6              # Last digit of your STUDENT_ID
TOTAL_LOOPS = 9           # Total loop cycles from Task 14

# Extract first letter of engineer name and convert to ASCII
first_letter = ENGINEER[0]
A = ord(first_letter)     # ASCII value of first letter
B = SEED_NUM
C = TOTAL_LOOPS

# Compute verification hash
verification_hash = (A * B) - C

# Print all assessment data
print(f"First Letter ASCII (A): {A}")
print(f"SEED NUM (B): {B}")
print(f"Total Loops (C): {C}")
print(f"Verification Hash: {verification_hash}")
# Initialize
surname = "LIM"           
SEED_NUM = 6               
redacted_name = ""

# Process each character
for char in surname:
    if char in "AEIOU":
        redacted_name += str(SEED_NUM)
    else:
        redacted_name += char

# Output
print(f"Original Surname: {surname}")
print(f"Redacted Output: {redacted_name}")
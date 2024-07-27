uppercase_count = 0
lowercase_count = 0
digit_count = 0
while True:
    char = input("Enter a character (type '*' to end): ")
    if char == '*':
        break
    if char=='':
        break
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1

print("Uppercase count:", uppercase_count)
print("Lowercase count:", lowercase_count)
print("Digit count:", digit_count)

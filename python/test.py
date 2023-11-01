user_input = input("Enter a string: ")
modified_string = ""

# Initialize a flag to start with an uppercase character
uppercase_next = True

for char in user_input:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        if uppercase_next:
            if 'a' <= char <= 'z':
                modified_string += chr(ord(char) - ord('a') + ord('A'))
            else:
                modified_string += char
        else:
            if 'A' <= char <= 'Z':
                modified_string += chr(ord(char) - ord('A') + ord('a'))
            else:
                modified_string += char
        uppercase_next = not uppercase_next
    else:
        modified_string += char

print("Modified string:", modified_string)

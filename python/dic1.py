input_string = input("Enter a string: ")

# Convert the input string to lowercase for case-insensitive comparison
input_string = input_string.lower()

# Initialize an empty dictionary to store character frequencies
char_freq = {}

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is an alphabet letter
    if char.isalpha():
        # If the character is already in the dictionary, increment its count
        # Otherwise, add it to the dictionary with a count of 1
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

# Print the frequency of each character
print(char_freq)
ref_list = []

# Ask the user for input until they input "STOP"
while True:
    user_input = input("Enter a number (type 'STOP' to end): ")

    # Check if the user wants to stop
    if user_input == "STOP":
        break

    # Convert the user input to an integer and add it to ref_list
    number = int(user_input)
    ref_list.append(number)

# Create a list 'frequency' containing sublists with the number and its count in ref_list
frequency = []

# Iterate over each unique number in ref_list
for num in ref_list:
    # Count the occurrences of the current number in ref_list
    count = ref_list.count(num)
    # Create a sublist containing the number and its count, and append it to the frequency list
    frequency.append([num, count])

# Sort the frequency list based on the numbers
frequency = sorted(frequency, key=lambda x: x[0])

# Initialize an empty list to store unique items from the frequency list
sorted_frequency = []

# Loop through the frequency list
for item in frequency:
    # Check if the item is not already in sorted_frequency
    if item not in sorted_frequency:
        # If not, append the item to sorted_frequency
        sorted_frequency.append(item)

# Print the sorted frequency list with the counts
for inpt, outpt in sorted_frequency:
    print(f"{inpt} - {outpt} times")

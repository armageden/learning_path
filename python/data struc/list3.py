# Input the first list from the user
list_1 = []
user_input = input("Enter the first list of numbers separated by spaces: ")
# Split the user input by spaces and convert each element to an integer, then append to list_1
for num_str in user_input.split():
    num = int(num_str)
    list_1.append(num)

# Input the second list from the user
list_2 = []
user_input = input("Enter the second list of numbers separated by spaces: ")
# Split the user input by spaces and convert each element to an integer, then append to list_2
for num_str in user_input.split():
    num = int(num_str)
    list_2.append(num)

# Initialize an empty list to store the cross multiplication product
result = []

# Iterate through each element of the first list
for i in list_1:
    # Iterate through each element of the second list
    for j in list_2:
        # Multiply the current element from the first list with each element from the second list
        # and append the result to the result list
        result.append(i * j)

# Print the resulting list containing the cross multiplication product
print(result)

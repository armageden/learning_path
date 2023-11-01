#home task 1 lab 4
str1 = input()
result = ""
i = 0
while i < len(str1):
    result += str1[i]
    j = i + 1

    while j < len(str1) and str1[j] == str1[i]:
        j += 1

    i = j

print(result)

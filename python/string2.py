#home task 2 lab 4
string = input()
string1 = ""
string2 = ""
comma = 0

for i in range(len(string)):
    if string[i] == "," and i < len(string) - 1 and string[i + 1] == " ":
        comma = i + 2
        break
    string1 += string[i]

string2 = string[comma:]
x = 0
y = 0
result = ""

while x < len(string1) and y < len(string2):
    result += string1[x] + string2[y]
    x += 1
    y += 1

result += string1[x:]
result += string2[y:]

print(result)
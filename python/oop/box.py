class box:
    def __init__(self, dim):
        self.height, self.width, self.breadth = dim
        print ("Creating a Box!")


# Write your class code here


print("Box 1")
b1 = box([10, 10, 10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30, 10, 10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")
one = b3 == b2
b3.width = 100
two = (b3 == b2)
print(one)
print(two)
print(b2.width)


#     one = (b3 == b2): This line compares the objects b3 and b2 for equality. Since b3 is assigned to b2, they both refer to the same object. Therefore, one will be True.

#     b3.width = 100: This line changes the width attribute of the b3 object to 100. Since b3 and b2 refer to the same object, the width attribute of b2 will also change to 100.

#     two = (b3 == b2): This line compares b3 and b2 again for equality. After changing the width attribute of b3, b3 and b2 are still referring to the same object. So, two will be True.

# As for the value of b2.width, it will be 100. Yes, the value has changed since the driver code ran because the width attribute of the shared object (b2 and b3) was modified later in the code. So, any reference to that object, including b2, reflects this change.

"""
Chapter 4: Lists & Tuples
"""

# -------------------------------
# 🔹 Lists
# -------------------------------
friends = ["Arnish", "Mitadru", 244444.09, False]
friends[0] = "Somarko"

print("First friend:", friends[0])
print("Third element:", friends[2])
print("Slice:", friends[1:3])

friends.append("Rohit")
print("Updated list:", friends)

# Sorting
numbers = [1, 2, 3, 4, 5, 11, 69, 67, 90]
numbers.sort()
print("Sorted:", numbers)

# Reverse
nums = [2, 6, 1, 10, 9]
nums.reverse()
print("Reversed:", nums)

# Insert
nums.insert(2, 100)
print("After insert:", nums)

# Pop
nums.pop(1)
print("After pop:", nums)

# Remove
nums.remove(10)
print("After remove:", nums)

# -------------------------------
# 🔹 Tuples
# -------------------------------
t = (100, False, "Arnish", 3333333, "Cow", True)
print("Type:", type(t))

print("Count of 100:", t.count(100))

t2 = (1, 2, 3, 2, 4, 2)
print("Count of 2:", t2.count(2))
print("Index of 2:", t2.index(2))

# Tuple immutability
try:
    t2[0] = 10
except TypeError:
    print("Tuples are immutable")

# -------------------------------
# 🔹 Practice
# -------------------------------

# Question 1
fruits = []
for i in range(7):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

print("Fruits:", fruits)

# Question 2
marks = []
for i in range(6):
    mark = int(input("Enter marks: "))
    marks.append(mark)

marks.sort()
print("Sorted marks:", marks)

# Question 3
t = (1, 2, 3)
try:
    t[0] = 5
except TypeError:
    print("Tuple cannot be changed")

# Question 4
numbers = [1, 2, 3, 4]
print("Sum:", sum(numbers))

# Question 5
t = (0, 1, 2, 3, 0, 4, 5, 0)
print("Zeros count:", t.count(0))

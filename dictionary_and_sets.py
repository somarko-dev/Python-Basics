 ==================
# Dictionary Methods
# ==================

marks = {
    "Somarko": 100,
    "Arnish": 98,
    "Soham": 89,
    "Anindya": 90,
}

print(marks, type(marks))
print(marks["Somarko"])
# print(marks[100])  # This code will not work.

# Methods
marks = {
    "Somarko": 100,
    "Arnish": 98,
    "Soham": 89,
    "Anindya": 90,
    0: "Raj"
}

print(marks.items())
print(marks.values())

marks.update({"Soham": 90})

print(marks.get("Tuhin"))
print(marks.keys())
print(marks.get("Soham2"))      # Returns None if the key doesn't exist.
# print(marks["Soham2"])        # Raises KeyError if the key doesn't exist.

# 1. get()
student = {"name": "Somarko", "age": 20}
print(student.get("name"))
print(student.get("marks"))      # Returns None
print(student.get("marks", 0))   # Returns 0 if key doesn't exist

# 2. update()
student = {"name": "Arnish"}
student.update({"age": 20})
print(student)

# 3. setdefault()
student = {"name": "Soham"}
student.setdefault("age", 18)
print(student)

# 4. copy()
student = {"name": "Mitadru"}
new_student = student.copy()
print(new_student)

# 5. clear()
student = {"name": "Priyanka", "age": 20}
student.clear()
print(student)

# 6. popitem()
student = {"name": "Basab", "age": 20}
item = student.popitem()  # Removes and returns the last inserted key-value pair.
print(item)
print(student)

# 7. fromkeys()
keys = ["name", "age", "city"]
student = dict.fromkeys(keys, "Unknown")
print(student)

# ======
# Sets
# ======

s = {1, 2, 3}
e = set()  # Don't use {} as it creates an empty dictionary.
print(s)

s = {1, 2, 2, 1, 1, 55, 54, "Soham"}
print(s, type(s))

s.add(51)
print(s)

# 1. update()
fruits = {"apple", "banana"}
fruits.update(["mango", "orange"])
print(fruits)

# 2. remove()
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)

# 3. discard()
fruits = {"apple", "banana"}
fruits.discard("grape")  # No error if the item doesn't exist.
print(fruits)

# 4. pop()
fruits = {"apple", "banana", "mango"}
item = fruits.pop()  # Removes an arbitrary element because sets are unordered.
print(item)
print(fruits)

# 5. clear()
fruits = {"apple", "banana"}
fruits.clear()
print(fruits)

# 6. copy()
fruits = {"apple", "banana"}
new_set = fruits.copy()
print(new_set)

# 7. union()
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

# 8. intersection()
print(a.intersection(b))

# 9. difference()
b = {2, 4}
print(a.difference(b))

# 10. symmetric_difference()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))

# 11. issubset()
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# 12. issuperset()
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))

# 13. isdisjoint()
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

# =================
# Practice Questions
# =================

# 1. Create a dictionary of Hindi words and look up their English meanings.

words = {
    "Billi": "Cat",
    "Machli": "Fish",
    "Kursi": "Chair"
}

word = input("Enter the Hindi word: ")
print(words.get(word, "Word not found"))

# 2. Input eight numbers and display only the unique numbers.

s = set()

for i in range(8):
    n = int(input(f"Enter number {i + 1}: "))
    s.add(n)

print(s)

# 3. Can a set contain both 18 (int) and "18" (str)?
s = set()
s.add(18)
s.add("18")
print(s)

# 4. What will be the length of the following set?

s = set()
s.add(20)
s.add(20.0)
s.add("20")

# 20 and 20.0 are considered equal in Python.
print(len(s))

# 5. Create a dictionary of four friends and their favourite languages.

d = {}

for i in range(4):
    name = input("Enter friend's name: ")
    lang = input("Enter favourite language: ")
    d.update({name: lang})

print(d)

# 6. If the names of two friends are the same,
# the last value overwrites the previous one.

# 7. If two friends choose the same language,
# nothing happens because dictionary values can be duplicated.

# 8. Can you change the values inside a list contained in a set?
# s = {8, 7, 12, "Somarko", [1, 2]}
# Answer:
# No. A Python set can only contain hashable (immutable) objects.
# A list is mutable, so it is unhashable and cannot be added to a set.

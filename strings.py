# Chapter 3: Strings 

"""
Chapter 3: Strings

This file covers:
- String slicing
- String methods
- Formatting
- Escape sequences
- Practice problems
"""

# -------------------------------
# 🔹 Basic Slicing
# -------------------------------
name = "Somarko"

print("First 4 letters:", name[0:4])
print("Negative slicing:", name[-4:-1])
print("Single character:", name[5])

word = "Programming"
print("Slice (1:5):", word[1:5])

# -------------------------------
# 🔹 String Properties
# -------------------------------
sentence = "programming is fun"

print("Length:", len(sentence))
print("Ends with 'ing':", sentence.endswith("ing"))
print("Ends with 'rko':", sentence.endswith("rko"))
print("Starts with 'pro':", sentence.startswith("pro"))
print("Starts with 'rko':", sentence.startswith("rko"))
print("Capitalized:", sentence.capitalize())

# -------------------------------
# 🔹 Split and Replace
# -------------------------------
text = "Hello,I am Somarko and I like chocolate"
print("Split by comma:", text.split(","))

text = text.replace("chocolate", "pizza")
print("After replace:", text)

# -------------------------------
# 🔹 Case Transformations
# -------------------------------
text = "hello world"

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Swapcase:", text.swapcase())

# -------------------------------
# 🔹 Searching & Counting
# -------------------------------
text = "programming is fun"

print("Starts with 'pro':", text.startswith("pro"))
print("Ends with 'fun':", text.endswith("fun"))
print("Find 'is':", text.find("is"))   # safe
print("Count 'm':", text.count("m"))

# -------------------------------
# 🔹 Replace Example
# -------------------------------
text = "I like Pizza Sprite"
print("Replace:", text.replace("Pizza", "Pizza and Sprite"))

# -------------------------------
# 🔹 Split & Join
# -------------------------------
text = "apple,banana,mango"
split_text = text.split(",")
joined = "-".join(split_text)
print("Joined:", joined)

# -------------------------------
# 🔹 Strip Spaces
# -------------------------------
text = "   hello   "
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())

# -------------------------------
# 🔹 String Checks
# -------------------------------
text = "12345"

print("Is Digit:", text.isdigit())
print("Is Alpha:", text.isalpha())
print("Is Alnum:", text.isalnum())
print("Is Space:", text.isspace())
print("Is Lower:", text.islower())
print("Is Upper:", text.isupper())

# -------------------------------
# 🔹 f-string Formatting
# -------------------------------
name = "Somarko"
age = 20
print(f"My name is {name} and I am {age} years old")

# -------------------------------
# 🔹 Length
# -------------------------------
test = "Hello Guys"
print("Length:", len(test))

# -------------------------------
# 🔹 Alignment
# -------------------------------
text = "hi"
print("Center:", text.center(10, "-"))
print("Left Justify:", text.ljust(10, "-"))
print("Right Justify:", text.rjust(10, "-"))

# -------------------------------
# 🔹 Advanced String Manipulation
# -------------------------------
text = "  python it is AWESOME to LEARN "

print("Clean lower:", text.strip().lower().replace("awesome", "a fun thing"))
print("Capitalized:", text.strip().capitalize())
print("Upper:", text.strip().upper())

# -------------------------------
# 🔹 Escape Sequences
# -------------------------------
print("Hello\nWorld")
print("Hello\tWorld")
print("Backslash: \\")
print("It's Python")
print("Hello\rWorld")
print("Hello\bWorld")
print("\u2764")

print("Name:\tSomarko\nRole:\tCybersecurity Student")

print(r"C:\newfolder")
print(r"C:\Users\Somarko")

# -------------------------------
# 🔹 Practice Questions
# -------------------------------

# Question 1 Write a python program to display a user entered name followed by Good Afternoon using input () function.
user_name = input("Enter your name: ")
print(f"Good Afternoon {user_name}")

# Question 2 Write a program to fill in a letter template given below with name and date. 
# letter = Dear <|Name|>, 
# You are selected! 
# <|Date|> 
letter = "Dear <|Name|>,\nYou are selected!\n<|Date|>"
print(letter.replace("<|Name|>", "Somarko").replace("<|Date|>", "2056-06-30"))

# Question 3 Write a program to detect double space in a string. 
text = "This is a string with  double spaces."
print("Double space index:", text.find("  "))
print("Fixed text:", text.replace("  ", " "))

# Question 4 letter = "Dear Priyanka, I like pulao. Thanks!"
letter = "Dear Priyanka,\nI like pulao.\nThanks \u2764"
print(letter)

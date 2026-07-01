# ==========================
# IF-ELSE STATEMENTS
# ==========================

age = int(input("Enter your age: "))

if age < 0 or age > 150:
    print("You're entering an invalid age.")
elif age >= 18:
    print("You are of the age of consent.")
else:
    print("You are below the age of consent.")

# Even or Odd
if age % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# ===============================================================================
# Practice Set
# ===============================================================================

# 1. Find the greatest of four numbers.

a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if a1 >= a2 and a1 >= a3 and a1 >= a4:
    print("Greatest number is:", a1)
elif a2 >= a1 and a2 >= a3 and a2 >= a4:
    print("Greatest number is:", a2)
elif a3 >= a1 and a3 >= a2 and a3 >= a4:
    print("Greatest number is:", a3)
else:
    print("Greatest number is:", a4)

# 2. Check whether a student has passed or failed.
# Pass criteria:
# - Overall percentage >= 40%
# - At least 33 marks in each subject

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total_percentage = (marks1 + marks2 + marks3) / 3

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You're Pass!", total_percentage)
else:
    print("You're Failed!", total_percentage)

# 3. Detect spam comments.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ").lower()

if p1 in message or p2 in message or p3 in message or p4 in message:
    print("This is a spam message.")
else:
    print("This is not a spam message.")

# 4. Username length.

username = input("Enter username: ")

if len(username) < 10:
    print("Your username contains less than 10 characters.")
else:
    print("Your username contains 10 or more characters.")

# 5. Check whether a name is present in the list.

names = ["Somarko", "Soham", "Arnish", "Basab"]

name = input("Enter your username: ")

if name in names:
    print("You're in the list!")
else:
    print("You're not in the list.")

# 6. Grade Calculator.

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 90:
    print("Your grade is: Ex")
elif marks >= 80:
    print("Your grade is: A")
elif marks >= 70:
    print("Your grade is: B")
elif marks >= 60:
    print("Your grade is: C")
elif marks >= 50:
    print("Your grade is: D")
else:
    print("Your grade is: F")

# 7. Check whether a post talks about Harry.

post = input("Enter post: ")

if "harry" in post.lower():
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")

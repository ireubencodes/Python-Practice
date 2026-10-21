# Lists Practice

shopping = ["Rice", "Beans", "Eggs", "Milk"]

print(shopping)
print(shopping[0])
print(shopping[-1])
print(len(shopping))

# List methods
students = ["Reuben", "John", "Amaka", "Tunde", "Chioma"]

# Add a student
students.append("Israel")
print(students)

# Remove a student
students.remove("John")
print(students)

# Loop through all students
for student in students:
    print(f"Student: {student}")

# Check if someone is in the list
print("Reuben" in students)
print("John" in students)
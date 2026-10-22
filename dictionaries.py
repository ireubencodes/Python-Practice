# Dictionaries Practice

student = {
    "name": "Reuben",
    "age": 24,
    "city": "Abuja",
    "is_student": True
}

# Access values
print(student["name"])
print(student["age"])
print(student.get("email", "No email found"))

# Add and update
student["email"] = "reuben@gmail.com"
student["age"] = 25
print(student)

# Loop through
for key, value in student.items():
    print(f"{key}: {value}")

# Check if key exists
print("name" in student)
print("phone" in student)
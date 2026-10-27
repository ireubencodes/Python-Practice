# Student Management System

students = []

def add_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)

def view_students():
    for student in students:
        print(f"Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

def search_student(name):
    for student in students:
        if student["name"] == name:
            print(f"Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
            return
    print("Student not found")

def remove_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student removed")
            return
    print("Student not found")

# Add students
add_student("Reuben", 24, "A")
add_student("John", 22, "B")
add_student("Amaka", 21, "A")

search_student("John")
search_student("Tunde")

remove_student("John")
remove_student("Tunde")
view_students()
# Sets Practice

visitors = {"Reuben", "John", "Amaka", "Reuben", "John"}
print(visitors)
print(len(visitors))

# Add and remove
visitors.add("Tunde")
print(visitors)

visitors.remove("John")
print(visitors)

# Check membership
print("Reuben" in visitors)
print("John" in visitors)

# Set operations
python_students = {"Reuben", "John", "Amaka"}
javascript_students = {"John", "Tunde", "Amaka"}

print(python_students | javascript_students)   # union
print(python_students & javascript_students)   # intersection
print(python_students - javascript_students)   # difference
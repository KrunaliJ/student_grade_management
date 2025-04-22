
# Student data: (name, subject, grade)
student1 = ("Alice", "Math", 85)
student2 = ("Bob", "Science", 90)
student3 = ("Charlie", "English", 78)

#  1. Accessing Tuple Elements
print("Accessing name and grade of student1:")
print("Name:", student1[0])
print("Grade:", student1[2])

#  2. Unpacking Tuples
name, subject, grade = student2
print(f"\nUnpacked student2: {name} is studying {subject} and scored {grade}")

#  3. Updating Tuples (Tuples are immutable, so recreate)
print("\nUpdating Charlie's grade to 82...")
student3 = (student3[0], student3[1], 82)
print("Updated student3:", student3)

#  4. Looping through Tuples (FOR loop)
students = (student1, student2, student3)

print("\nListing all students using for loop:")
for student in students:
    print(f"{student[0]} scored {student[2]} in {student[1]}")

#  5. Looping through Tuples (WHILE loop)
print("\nListing all students using while loop:")
i = 0
while i < len(students):
    s = students[i]
    print(f"{s[0]} has {s[2]} in {s[1]}")
    i += 1

#  6. Joining Tuples
grades = (85, 90, 82)
comments = ("Good", "Excellent", "Improved")

combined = grades + comments
print("\nJoined grades and comments tuple:", combined)

#  7. Tuple Methods
print("\nTuple Methods Demo:")
print("Number of times 85 appears in grades:", grades.count(85))
print("Index of 90 in grades:", grades.index(90))

# Bonus: Sort students by grade (convert to list for sorting)
print("\nSorted students by grade (high to low):")
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
for s in sorted_students:
    print(f"{s[0]} - {s[2]}")

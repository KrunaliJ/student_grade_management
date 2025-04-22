# student_grade_management

Part 1: Creating Tuples
# Student data: (name, subject, grade)
student1 = ("Alice", "Math", 85)
student2 = ("Bob", "Science", 90)
student3 = ("Charlie", "English", 78)
Each student is a tuple with 3 values: name, subject, and grade.
This shows how to create a tuple.

Part 2: Accessing Tuple Elements
print("Accessing name and grade of student1:")
print("Name:", student1[0])
print("Grade:", student1[2])
student1[0] gets Alice (name).
student1[2] gets 85 (grade).
This shows how to access specific elements in a tuple using indexing.

Part 3: Unpacking a Tuple
name, subject, grade = student2
print(f"\nUnpacked student2: {name} is studying {subject} and scored {grade}")
This breaks student2 into 3 variables: name, subject, grade.
It's called tuple unpacking.
Makes it easy to access parts of the tuple by variable name instead of index.

Part 4: Updating a Tuple
print("\nUpdating Charlie's grade to 82...")
student3 = (student3[0], student3[1], 82)
print("Updated student3:", student3)
Tuples are immutable (can’t be changed directly).
So to "update" it, we create a new tuple using parts of the old one and a new grade.

Part 5: FOR Loop over Tuple of Tuples
students = (student1, student2, student3)
print("\nListing all students using for loop:")
for student in students:
    print(f"{student[0]} scored {student[2]} in {student[1]}")
students is a tuple of all three student tuples.
We use a for loop to go through each student.
Each student is itself a tuple, so we access elements using indexes.

Part 6: WHILE Loop over Tuple
print("\nListing all students using while loop:")
i = 0
while i < len(students):
    s = students[i]
    print(f"{s[0]} has {s[2]} in {s[1]}")
    i += 1
This does the same as the for loop above, but uses a while loop.
i is the loop counter, starting at 0.
We loop while i is less than the number of students.

Part 7: Joining Tuples
grades = (85, 90, 82)
comments = ("Good", "Excellent", "Improved")

combined = grades + comments
print("\nJoined grades and comments tuple:", combined)
+ is used to join tuples.
The combined tuple contains all elements from grades and comments.

Part 8: Tuple Methods
print("\nTuple Methods Demo:")
print("Number of times 85 appears in grades:", grades.count(85))
print("Index of 90 in grades:", grades.index(90))
.count(value) tells how many times a value appears in the tuple.
.index(value) gives the first position of the value in the tuple.

Bonus: Sorting (Even though Tuples can’t be sorted directly)
print("\nSorted students by grade (high to low):")
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
for s in sorted_students:
    print(f"{s[0]} - {s[2]}")
sorted() is used to sort based on grade (which is at index 2 in each student tuple).
lambda x: x[2] means: sort using the third element (grade).
reverse=True sorts in descending order.












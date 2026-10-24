marks = [85, 74, 98, 73, 69]

# positive traversing
"""for mark in marks:
    print(mark)

for i in range(len(marks)):
    print(marks[i])"""


# negative traversing
"""for mark in reversed(marks):
    print(mark)

for mark in marks[:: -1]:
    print(mark)

for mark in range(len(marks) -1, -1, -1):
    print(marks[mark])"""


# nested Loops

# It is o(n^2) -> bad way
stu_marks = [
    [85, 89, 95],
    [90, 97, 99],
    [79, 99, 97]
]

for mark in stu_marks:
    for nums in mark:
        print(nums, end= " ")
    print()
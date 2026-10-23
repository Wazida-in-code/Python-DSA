marks = [85, 74, 98, 73, 69, 99]

# access
"""print(marks[2]) # O(1)
print(marks[5])"""

# insert
"""marks.append(55) # O(1) add in the end
marks.insert(2, 55) # O(n) add anywhere"""


# delete
"""marks.pop() # delete last item O(1)
marks.pop(3) #delete any item O(n)
marks.remove(69) #delete item by value O(n)"""


# O(k)-> slicing
print(marks[1:4])
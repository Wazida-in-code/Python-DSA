def find_Duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i != j) and numbers[i] == numbers[j]:
                return True
    return False

numbers = [21, 28, 18, 27, 21, 9]

result = find_Duplicate(numbers)

if result:
    print("Found Duplicate!")
else:
    print("Not Found Duplicate!")
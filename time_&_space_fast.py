def has_duplicate_fast(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

numbers = [21, 28, 18, 27, 21, 9]
result = has_duplicate_fast(numbers)

if result:
    print("Found dupliacte!")
else:
    print("Not found duplicate!")
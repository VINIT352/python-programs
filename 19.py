
numbers = (1, 2, 3, 4, 5, 2, 4, 6, 7, 7)
repeated_numbers = []

for num in numbers:
    if num in repeated_numbers:
        continue
    
    if numbers.count(num) > 1:
        repeated_numbers.append(num)

print("Repeated numbers:", repeated_numbers)

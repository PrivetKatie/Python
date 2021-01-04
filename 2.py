numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_numbers = [el for i, el in enumerate(numbers) if numbers[i - 1] < numbers[i]]


print(new_numbers)
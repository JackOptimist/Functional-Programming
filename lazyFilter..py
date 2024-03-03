def lazy_filter(sequence, condition):
    for item in sequence:
        if condition(item):
            yield item

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = lazy_filter(numbers, lambda x: x % 2 == 0)

print("Even numbers:")
for num in even_numbers:
    print(num)

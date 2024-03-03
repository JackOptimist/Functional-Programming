def max_path(pyramid, level=0, index=0):
    if level == len(pyramid) - 1:
        return pyramid[level][index]

    left_path = max_path(pyramid, level + 1, index)
    right_path = max_path(pyramid, level + 1, index + 1)

    return pyramid[level][index] + max(left_path, right_path)

pyramid = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

print("The maximum path from the top to the base of the pyramid:", max_path(pyramid))

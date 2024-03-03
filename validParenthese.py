def generate_valid_parentheses(n):
    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            result.append(curr)
            return
        if open_count < n:
            backtrack(curr + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result

n = 3
valid_parentheses = generate_valid_parentheses(n)
for seq in valid_parentheses:
    print(seq)

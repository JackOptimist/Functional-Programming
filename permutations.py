def generate_permutations(lst):
    if len(lst) <= 1:
        return [lst]
    
    result = []
    for i, el in enumerate(lst):
        rest = lst[:i] + lst[i+1:]
        for perm in generate_permutations(rest):
            result.append([el] + perm)
    return result

my_list = [1, 2, 3]
perms = generate_permutations(my_list)
for perm in perms:
    print(perm)

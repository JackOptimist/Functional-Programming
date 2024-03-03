
def find_element(list, target):
    if not list:
        return False
    elif list[0] == target:
        return True
    else:
        return find_element(list[1:], target)

list = [1, 2, 3, 4, 5]
target = 3

print(find_element(list, target))
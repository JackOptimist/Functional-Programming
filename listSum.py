
def listSum(list):

    if not list:
        return 0
    else:
        return list[0] + listSum(list[1:])

list = [1, 2, 3, 4, 5]
print(listSum(list))

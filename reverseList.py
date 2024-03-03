def reverse_list(list):
    if len(list) == 0:
        return[]
    else:
        return [list[-1]] + reverse_list(list[:-1])
    

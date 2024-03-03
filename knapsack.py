def knapsack(weights, values, capacity):
    memo = {}

    def knapsack_helper(index, current_capacity):

        if index < 0 or current_capacity == 0:
            return 0
        
        if (index, current_capacity) in memo:
            return memo[(index, current_capacity)]
        
        if weights[index] > current_capacity:
            memo[(index, current_capacity)] = knapsack_helper(index - 1, current_capacity)
            return memo[(index, current_capacity)]
        
        included = values[index] + knapsack_helper(index - 1, current_capacity - weights[index])
        not_included = knapsack_helper(index - 1, current_capacity)

        memo[(index, current_capacity)] = max(included, not_included)
        return memo[(index, current_capacity)]
    
    return knapsack_helper(len(weights) - 1, capacity)

weights = [2, 4, 1]
values = [1000, 900, 50]
capacity = 5
print(knapsack(weights, values, capacity))


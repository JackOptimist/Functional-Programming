def power_generation_function(power):
    def power_function(n):
        return n ** power
    return power_function

square = power_generation_function(2)
cube = power_generation_function(3)

print(square(5))
print(cube(5))
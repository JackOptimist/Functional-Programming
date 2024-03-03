from functools import reduce

# function that converstion celcius to fahrenheit and filtered temperature in list, than return average value of current list (filtered list)
def temperature_conversion(temperatures):
    celcius_to_fahrenheit = map(lambda x: x * 1.8 + 32, temperatures) # f = C * 1.8 + 32
    freezing_points = filter(lambda x: x < 32, celcius_to_fahrenheit) # freeze point = 32, filtered list

    freezing_points_list = list(freezing_points) # boxing to iterator to list

    average_value = reduce(lambda x, y: x + y, freezing_points_list, 0) / len(freezing_points_list) # average value
    return average_value

celcius_temperatures = [25, -10, 0, 15, 30, -5, 10, 20, -15, 5]
celcius_to_fahrenheit = map(lambda x: x * 1.8 + 32, celcius_temperatures) 
less_than_freezing_point = filter(lambda x: x < 32, celcius_to_fahrenheit)

filtered_list = list(less_than_freezing_point)
average_value = temperature_conversion(celcius_temperatures) # call our function

print(filtered_list) # display to see and check
print(average_value) # our result
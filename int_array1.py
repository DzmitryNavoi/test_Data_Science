def unique_sorted_values(input_array):
    unique_sorted_array = sorted(list(set(input_array)))
    return unique_sorted_array

input_array = [3, 1, 2, 2, 8,10, 23, 4,4, 0.5, 4, 3, -1]

for i, item in enumerate(input_array):
    input_array[i] = int(item)

result = unique_sorted_values(input_array)
print(result)
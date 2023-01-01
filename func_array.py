
def max_array(my_array):

    max_sum = my_array[0]
    for item in my_array:
        if item < max_sum:
            item = max_sum

    return max_sum

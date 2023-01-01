
<<<<<<< HEAD
def max_array(my_array):

    max_sum = my_array[0]
    for item in my_array:
        if item < max_sum:
            item = max_sum

    return max_sum

======= Добавлено из ветки var_1

def sum_array(my_array):
    ind = 0
    sum = 0
    while ind < len(my_array):
        sum = sum + my_array[ind]
    return sum
    
>>>>>>> var_2

# Take an array with postieve and 
# neg int and find 
# the max sum of the array


def largest(arr):
    if len(arr) == 0:
        return print('Too small')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        # similar to a current sum tracker 

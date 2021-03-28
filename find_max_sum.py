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
        max_sum = max(current_sum, max_sum)
        # largest continual sum

    return max_sum
    # that is why memorzing fundmental algorthims 
    # is important do not re-invente the wheel!!!
    # strong foundations if these are memorzied

print(largest([7, 1, 2, -1, 4, 10, -12, 3, 21, -19]))
# the largest running sum


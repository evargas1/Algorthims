ef pair_sum(array, k):
    # not an actual array probs called it that 
    # because similar to arrays all the #s 
    # where the same 
    if len(array) < 2:
        return print('Too Small')
    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
# time complexity == O(n**2)
    print("\n".join(map(str, list(output))))



pair_sum([1,3,2,2], 4)
# this function is not only for arrays it can be used to solve
# other forms of list rather its tuples lists or strings


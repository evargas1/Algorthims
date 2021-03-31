# Given 2 arrays (assume no duplications) is 1 array 
# a rotation of another -- return True/ False
# same size and elements but start index is different


# BigO we are going through each array 2x but O(2n) = O(n)
# sinice infinate sized lists, constants means nada

# select an indexed posistion in list1 and gets its value
# Find some element in list2 and check index for index from there
# if any variation then we know its false 
# Getting to last item without a false means true.


def rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_index = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i

            break

    if key_index == 0:
        return False

    for x in range(len(list1)):
        l2index = (key_index + x) % len(list1)

        if list1[x] != list2[l2index]:
            return False
    return True

print(rotation([1, 2, 3], [2, 1, 3]))






        

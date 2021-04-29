# """
# Given an array what is the most frequently occuring element
# """
# # checks the occurence of a number not the actual value of that intger

# def most_frequent(list):
#     count = {}
#     max_count = 0
#     max_item = None

#     for i in list:
#         if i not in count:
#             count[i] = 1

#         else:
#             count[i] += 1

#         if count[i] > max_count:
#             max_count = count[i]
#             max_item = i
#     return max_item

# print(most_frequent([1,3,3,3,2,1,1,1]))


def least_frequent(list):
    store = {}
    least_occurnces = 0
    num = None

    for i in list:
        if i not in store:
            store[i] = -1
        else:
            store[i] -= 1
        if store[i] < least_occurnces:
            store[i] = least_occurnces
            num = i
    return num

print(least_frequent([1,2,2,3,3,3]))
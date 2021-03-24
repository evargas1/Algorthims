arr = [31, 41, 59, 26, 41, 58]

value = 41

for i in range(1, len(arr)):
        # print(i)
        # is index posistion
        print(i)
 
        key = arr[i]
        print(key)
        # actual value 
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        # j tranforms index into computer binary form starting 0 
        
        while j >= 0 and key < arr[j] :
                print(arr[j])
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

print(arr)

# for i in range(1, len(arr)):
       
#         # is index posistion
 
#         key = arr[i]
       
        # actual value 
#         if key == value:
#                 print("Your number: " + str(value) + " is in the list")


# value_number = [x for x in arr if x == value]
# print(value_number)

# you have two list and you add the numbers together accroding
# to there index posistion

# list_1 = [45, 7, 9, 1]
# list_2 = [20, 33, 8, 2]        
# active = True
# while active:
#         added_up = list_1[0] +list_2[0]
#         print(added_up)
#         active = False

# check_1 = []
# for x, y in range(1, len(list_1)), range(1, len(list_2)):
#         print(x)
#         print(y)

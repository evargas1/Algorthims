"""

Linear time solution 

Non repeat element
Take a string and return characters that never repeats if mutiple unique 
then only return only the first 
unique character 

This algo is really helpful in 
cyber sercuity!


"""

def non_repeating(s):
    s = s.replace(' ', '').lower()

    char_count = {}
    # answer = set()
    # could make this a set and use 
    # the add varaible or you could
    # make it an empty list and 
    # append the letter 
    # but i think set works better
    # to catch erros

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
        
    # for c in s:
    #     if char_count[c] == 1:
    #         answer.add(c)

    answer = [ c for c in s if char_count[c]==1]



    return answer



print(non_repeating('I apple Love eating'))


def non(s):
    char_count = {}
    s = s.replace(' ', '').lower()

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    unique = []
    y = sorted(
        char_count.items(),
        key=lambda x: x[1]
        # will sort by second
        # tuple posistion in this
        # case the value
    )
    print(y[0])
    print(y)
    

    for item in y:
        # checking the index 
        # posistion of 1 now a tuple
        # which use to be the value
        # or number
        print(item)
        if item[1] == y[0][1]:
            # [0] first value
            # [1] the value in the first key value
            
            # index posistion?
            unique.append(item)

    return unique

print(non('uuu iiiiiikkkkkklllll'))

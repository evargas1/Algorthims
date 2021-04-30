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


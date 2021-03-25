import sys

n = 10
data = []
for i in range(n):
    
    # seems to be starting at 0
    a = len(data)
    b = sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d}'. format(a,b))
    data.append(n)
    # this ran to slo wit was a O(n) running in linear time



    # my anagramp exmaple 
def anagram(s1, s2):
        # remove the spaces and lowcase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    print(sorted(s1), sorted(s2))
    # the sorted function is what helped us find the answer!

    return sorted(s1) == sorted(s2)
    

print(anagram('cast', 'saCt'))
# not the best solution because it is using a python module .replcace


def inter_anagram(s1, s2):
    """will check to see if two strings are a secert message"""
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
             count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False


    return True 
    
# good practice to build an anagram from scratch may be 
# asked a job intervidw
print(inter_anagram('god', 'dog'))


# Given a integer array output all the unique pairs that sum up to a specfic value k.
# so the input 
# pair_sum ([1,3,2,2], 4)
#    would return 2 pairs 
# (1,3)
# (2,2)

def pair_sum(array, k):
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

    print("\n".join(map(str, list(output))))



pair_sum([1,3,2,2], 4)
# this function is not only for arrays it can be used to solve
# other forms of list rather its tuples lists or strings







        
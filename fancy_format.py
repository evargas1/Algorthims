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
    


print(inter_anagram('god', 'dog'))






        
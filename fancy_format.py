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

        return sorted(s1) == sorted(s2)

        
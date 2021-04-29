"""
Given a string are all the characters unique?
Should return a True or False return


uses python built in structures
"""

def unique(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)
    # set don't include repeats?
    # they only include unique elements

print(unique('a b cdef'))


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

"""
solve this same problem but you cant
use the built in functions

"""
def unique_no(s):
    s = s.replace(' ', '')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

print(unique_no('hok sj'))


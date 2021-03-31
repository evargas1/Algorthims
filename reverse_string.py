# Given a string of words revser all the words
# star = "This is the best"
# end = "tseb eht si siht"

def reverse(s):
    s = s.split()
    s.reverse()
    # python built in functions 


    return s

print(reverse("This is the best"))

# alternative shorter way to write 
def sec_reverse(s):
    return "-".join(reversed(s.split()))
    # simialr to list comphensions
    # what is the differn=ence between reverse and reversed

print(sec_reverse("trying a shorter function"))

ex = "this is an intreasting method"
print(reverse(ex))
# print(reversed(ex))
# reversed is for an object 
# reverse is for a string 

def index_reverse(s):
    return " * ".join(s.split()[::-1])

print(index_reverse("This is the best"))


def len_revsrse(s):

    length = len(s)
    spaces = [' ']
    words = []
    # include spaces
    i = 0
    # index counter
    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])
            # word start or 0 to i
        i += 1


    return "".join(reversed(s))


print(len_revsrse("This is Wack"))

def ex_rev(s):
    return s.split()[::-1]
    # indexing is used a lot in AI and data science 
    # to muniplate large amouts of data
print(ex_rev('Hello I am grant'))







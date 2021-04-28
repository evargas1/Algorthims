# given a string of words reverse all the words

# start = "This is the best"
# finish = "best the is this"

def reverse(s):
    s = s.split()
    # assuming you cant used the split function
    s.reverse()
    # the split function divides the words according to the spaces
    return "-".join(s)

print(reverse("This is the best"))

def alternate_reverse(s):
    return " + ".join(s.split()[::-1])
    # classic indexing from beginng to the end and than reverse
    # it with the -1

print(alternate_reverse("This is the best"))


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
            # intializes and 
            # will begin the reverseing process
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
            # word start or 0 to i
        i += 1


    return " ".join(words[::-1])

print(len_revsrse("This better work no spilt or reverse"))

def extreme(s):
    
    return "".join(reversed(s))

print(extreme("This should not work right?"))
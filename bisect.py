import bisect

l = [1, 3, 7, 5, 6, 4, 9, 8, 2]

result = []
for e in l:
    bisect.insort(result, e)

print(result)


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]
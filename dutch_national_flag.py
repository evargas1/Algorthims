"""
We start by forming 3 list (1) less than the pivot (2) elements equal to the pivot and (3) elements greater 
thna the pivot.

With this function we begin by iterating through A starting from index 0 searching for a values less than the pivot value.  As soon as we find it we move it to the subarray of smaller elements via an exchange. This function will move all values smaller than the pivot value to the start of the list. 

"""


def dutch(pivot_index, A):
    pivot = A[pivot_index]
    # first pass: group elements smaller than pivot 
    for i in range(len(A)):
        # look for a smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]


    for i in reversed(range(len(A))):
        # look for a larger element larger than pivot
        # pivot since first pass has moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

    return A

ans = dutch(4, [3, 9, 0, 5, 7, 1])
print(ans)


def national(pivot_index, A):
    pivot = A[pivot_index]
    # first pass: group elements smaller than the pivot 
    samller = 0 
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[samller] = A[samller], A[i]
            samller += 1
    # second pass: group elements larger than the pivot 
    larger = len(A) - 1 
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1 

    return A


r = national(1, [3, 2, 4, 1, 6, 3])
print(r)



def flag(pivot_index, A):
    pivot = A[pivot_index]
    # keep the following invariants during partionshing 
    # bottom group: A[:smaller]
    # middel group: A[smaller:eqaul]
    # unclassiified group: A[equal:larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    # keep iterating as long as there is an unclassified element
    while equal < larger:
        # A[equal] is to incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            # A[eqaul] > pivot 
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

    return A

s = flag(3, [2, 4, 6, 9, 8, 1])
print(s)


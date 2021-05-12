def sol(array, sequence):
    seqx = 0
    for value in array:
        if seqx == len(sequence):
            break
        if sequence[seqx] == value:
            seqx += 1
    return seqx == len(sequence)

	
	
print(sol([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))


def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# print(count_bits(9000000))

# functions to see how many bites are needed to represent a number. Effectively

def parity(x): 
    result = 0 
    while x:
        result ^= x & 1
        x >>= 1
    return result

print(parity(89000))

def abtru(x):
    result = 0 
    while x:
        result ^= 1
        x &= x - 1 
    return result


print(abtru(7900))
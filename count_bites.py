def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print(count_bits(90000000000))

# functions to see how many bites are needed to represent a number. Effectively
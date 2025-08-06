def scramble(strng, array):
    return ''.join([strng[array.index(i)] for i in range(len(strng))])
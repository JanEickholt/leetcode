def restoreString(s, indices):
    return ''.join(sorted(zip(indices, s), key=lambda x: x[0]))

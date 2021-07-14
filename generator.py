def sequence(start=0):
    while True:
        yield start
        start += 1


seq = sequence(102)
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

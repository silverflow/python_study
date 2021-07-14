sum_use_generator = sum((x ** 2 for x in range(10)))
print(sum_use_generator)

list_enumerate = list(enumerate("abcdefgh"))
print(list_enumerate)


class NumberSequence:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self


print(list(zip(NumberSequence(), "abcdef")))

class Noo:
    def __eq__(self, other):
        return False


foo = Noo()

print(foo == "True")
print(foo is None)

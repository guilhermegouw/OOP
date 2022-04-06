apples = [20, 4, 5, 10, 15]


class Sorted:
    def __init__(self, items):
        self.data = items

    def sort(self):
        self.data.sort()

    def get(self, index):
        return self.data[index]


def consummer1(basket):
    """Get the heaviest apple"""
    s = Sorted(basket)
    s.sort()
    return s.get(-1)


print(consummer1(apples))

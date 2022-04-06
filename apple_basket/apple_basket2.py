apples = [20, 4, 5, 10, 15]


class Sorted:
    def __init__(self, items):
        self.data = items

    def head(self):
        return max(self.data)


def consummer1(basket):
    """Get the heaviest apple"""
    s = Sorted(basket)
    return s.head()


print(consummer1(apples))

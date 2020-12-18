class Diflist:
    def __init__(self, item, support, list=[], initial=None):
        self.item = item
        self.support = support # should NOT be equal to 0

        if initial is None:
            self.list = []
        else:
            self.list = initial

    def push(self, item):
        self.list.append(item)
        self.support -= 1

    def __str__(self):
        return f"{self.list} (sup={self.support})"

    def __repr__(self):
        return f"{self.list} (sup={self.support})"

from dEclat.Itemset import Itemset

class Diflist:
    def __init__(self, itemset: Itemset, support: float, list=[], initial=None):
        self.itemset = itemset
        self.support = support # should NOT be equal to 0

        if initial is None:
            self.list = []
        else:
            self.list = initial

    def push(self, item):
        self.list.append(item)
        self.support -= 1

    def union(self, diflist):
        itemset = [*self.itemset.items, diflist.itemset.items[-1]]
        items = list(filter(lambda x: x not in self.list, diflist.list))
        support = self.support - len(items)
        return Diflist(Itemset(itemset), support, initial=items)

    def __str__(self):
        return f"({self.itemset}) {self.list} (sup={self.support})"

    def __repr__(self):
        return f"({self.itemset}) {self.list} (sup={self.support})"

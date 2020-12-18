from uuid import uuid4

class Itemset:
    def __init__(self, items=[]):
        self.items = items
        self.hash = uuid4()

    def add(self, item):
        it = Itemset(items=[*self.items, item])
        return it
        
    def __str__(self):
        return f"{self.items}"
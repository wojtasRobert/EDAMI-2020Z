class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Transaction:
    def __init__(self):
        self.items = []
        self.counter = 0

    def __str__(self):
        return f"Transaction: {self.items}"

    def __repr__(self):
        return f"Transaction: {self.items}"


    def push(self, item):
        self.items.append(item)
        self.counter += 1


class TransactionalDatabase:
    def __init__(self, df, items, transactions):
        self.df = df
        self.items = items
        self.transactions = transactions

    def __str__(self):
        return f"Transactional database of {len(self.items)} items with {len(self.transactions)} transactions"
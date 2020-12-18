from Transactional.Database import TransactionalDatabase, Transaction, Item
from dEclat.Control import dEclatControl
from dEclat.Diflist import Diflist

def createInitialTidlists(data: TransactionalDatabase):
    tidlists = {} 
    maxSupport = len(data.transactions)

    for item in data.items:
        tidlists[item.id] = Diflist(item, maxSupport)

    for transaction in data.transactions:
        for item in data.items:
            if item not in transaction.items:
                tidlists[item.id].push(transaction.id)
    
    return tidlists
    
def dEclat(data: TransactionalDatabase, params: dEclatControl):
    tidlists = createInitialTidlists(data)
    return tidlists

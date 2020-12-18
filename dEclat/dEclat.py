from Transactional.Database import TransactionalDatabase, Transaction, Item
from dEclat.Control import dEclatControl
from dEclat.Diflist import Diflist
from math import floor

def createInitialTidlists(db: TransactionalDatabase):
    tidlists = {} 
    maxSupport = db.size()

    for item in db.items:
        tidlists[item.id] = Diflist(item, maxSupport)

    for transaction in db.transactions:
        for item in db.items:
            if item not in transaction.items:
                tidlists[item.id].push(transaction.id)
    
    return tidlists

def filterFrequentItemsets(tidlists, threshold):
    return filter(lambda x: x[1].support > threshold, tidlists.items())
    
def dEclat(db: TransactionalDatabase, params: dEclatControl):
    frequentThreshold = floor(params.support * db.size())
    print(frequentThreshold)
    
    tidlists = createInitialTidlists(db)
    print(tidlists)
    
    print("---")

    tidlists = filterFrequentItemsets(tidlists, frequentThreshold)

    for tl in tidlists:
        print(tl)

    return tidlists

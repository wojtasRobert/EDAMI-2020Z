from Transactional.Database import TransactionalDatabase, Transaction, Item
from dEclat.Control import dEclatControl
from dEclat.Diflist import Diflist
from dEclat.Itemset import Itemset
from math import floor

def createInitialDiflists(db: TransactionalDatabase):
    diflists = {} 
    maxSupport = db.size()

    for item in db.items:
        diflists[item.id] = Diflist(Itemset(items=[item]), maxSupport)

    for transaction in db.transactions:
        for item in db.items:
            if item not in transaction.items:
                diflists[item.id].push(transaction.id)
    
    return diflists

def filterFrequentItemsets(diflists, threshold):
    filteredDiflists = {}
    for (idx, diflist) in diflists.items():
        if diflist.support >= threshold:
            filteredDiflists[idx] = diflist
            
    return filteredDiflists
    
def dEclat(db: TransactionalDatabase, params: dEclatControl):
    frequentThreshold = floor(params.support * db.size())

    diflists = createInitialDiflists(db)
    print(diflists)
    
    print("---")

    diflists = filterFrequentItemsets(diflists, frequentThreshold)
    print(diflists)

    print("Merging diflists")
    print(diflists[1].union(diflists[3]))

    return diflists

from Transactional.Database import TransactionalDatabase, Transaction, Item
from dEclat.Diflist import Diflist
from dEclat.Itemset import Itemset
from dEclat.Rules import Rule, Ruleset, InductionControl
from math import floor
import numpy as np

class dEclatControl:
    def __init__(self, support=0.1, minlen=1, maxlen=10, use_matrix=False, sort=False, sort_reverse=False):
        self.support = support
        self.minlen = minlen
        self.maxlen = maxlen

        self.use_matrix = use_matrix
        self.sort = sort
        self.sort_reverse = sort_reverse


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
    frequentItemsets = []
    
    diflists = createInitialDiflists(db)
    diflists = filterFrequentItemsets(diflists, frequentThreshold)

    if params.sort:
        diflists = dict(sorted(diflists.items(), key=lambda item: item[1].support))
    
    if params.sort_reverse:
        diflists = dict(sorted(diflists.items(), key=lambda item: item[1].support, reverse=True))

    if params.minlen <= 1:
        for diflist in diflists.values():
            frequentItemsets.append(diflist)

    if params.use_matrix:
        matrix = []
        for i, fi in enumerate(frequentItemsets):
            for j, fj in enumerate(frequentItemsets):
                if i == j or i > j:
                    continue
                matrix.append(fi.union(fj))
                
        diflists = {}
        for idx, candidate in enumerate(matrix):
            if candidate.support >= frequentThreshold:
                diflists[idx] = candidate
                

    def dEclatImpl(diflists, depth):
        if depth > params.maxlen or len(diflists.keys()) == 0:
            return

        next_it = {}
        for (key_i, diflist_i) in diflists.items():
            next_it[key_i] = {}; idx = 1
            for (key_j, diflist_j) in diflists.items():
                if key_i >= key_j:
                    continue
                
                new_diflist =  diflist_i.union(diflist_j)
                if new_diflist is not None:
                    next_it[key_i][idx] = new_diflist
                    idx += 1
    
            next_it[key_i] = filterFrequentItemsets(next_it[key_i], frequentThreshold)
            for diflist in next_it[key_i].values():
                if params.minlen <= depth:
                    frequentItemsets.append(diflist)

        for subset in next_it.values():
            dEclatImpl(subset, depth+1)

    dEclatImpl(diflists, 3 if params.use_matrix else 2)

    return frequentItemsets

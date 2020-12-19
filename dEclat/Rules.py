from Transactional.Database import TransactionalDatabase
from dEclat.Itemset import Itemset

class InductionControl:
    def __init__(self, confidence=0.5):
        self.confidence = confidence

class Rule:
    def __init__(self, lhs: Itemset, rhs: Itemset, support, confidence):
        self.lhs = lhs
        self.rhs = rhs
        self.support = support
        self.confidence = confidence

    def __str__(self):
        return f"{self.lhs} => {self.rhs} (sup={self.support}, conf={self.confidence})"

    def __repr__(self):
        return f"{self.lhs} => {self.rhs} (sup={self.support}, conf={self.confidence})"
    
class Ruleset:
    def __init__(self):
        self.rules = []

    def add(self, rule: Rule):
        self.rules.append(rule)

    def __str__(self):
        return f"{self.rules}"

    def __repr__(self):
        return f"{self.rules}"

def rulesInduction(frequentItemsets, db: TransactionalDatabase, params: InductionControl):
    ruleset = Ruleset()

    hashmap = {}
    for fi in frequentItemsets:
        hashmap[fi.itemset.hash] = fi

    for fi in frequentItemsets:
        if fi.length < 2:
            continue

        for item in fi.itemset.items:
            lhs = Itemset(items=[x for x in fi.itemset.items if x != item])
            rhs = Itemset(items=[item])

            lhs_support = hashmap[lhs.hash].support
            rhs_support = hashmap[rhs.hash].support

            if fi.support / lhs_support > params.confidence:
                ruleset.add(Rule(lhs=lhs, 
                                 rhs=rhs,
                                 support=fi.support / db.size(),
                                 confidence=fi.support / lhs_support)
                            )
    return ruleset

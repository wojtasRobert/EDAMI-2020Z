from Transactional import read_csv
from dEclat import dEclat, dEclatControl
from dEclat.Rules import rulesInduction, InductionControl

if __name__ == "__main__":
    # load data in transactional format
    db = read_csv("./data/mushrooms.csv")

    # mine frequent itemsets
    DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10)
    frequentItemsets = dEclat(db, DE_params)

    # induce rules from frequent itemsets
    RI_params = InductionControl(confidence=0.8)
    ruleset = rulesInduction(frequentItemsets, db, RI_params)
    for idx, rule in enumerate(ruleset.rules):
        print(f"{idx+1}. {rule}")

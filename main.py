from Transactional import read_csv
from dEclat import dEclat, dEclatControl
from dEclat.Rules import rulesInduction, InductionControl

if __name__ == "__main__":
    # load data in transactional format
    db = read_csv("./data/test.csv")

    # mine frequent itemsets
    DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10)
    frequentItemsets = dEclat(db, DE_params)

    # induce rules from frequent itemsets
    RI_params = InductionControl(confidence=0.5)
    ruleset = rulesInduction(frequentItemsets, db, RI_params)
    
    print(ruleset.as_data_frame())

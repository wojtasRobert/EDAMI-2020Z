import sys
from Transactional import read_csv
from dEclat import dEclat, dEclatControl

if __name__ == "__main__":
    db = read_csv("./data/mushrooms.csv")
    params = dEclatControl(support=0.5,minlen=1, maxlen=10)
    frequentItemsets = dEclat(db, params)
    frequentItemsets.sort(reverse=True, key=lambda x: x.support)

    for (idx, fi) in enumerate(frequentItemsets):
        print(f"[{idx+1}] {fi.itemset} ({fi.support})")     

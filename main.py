from Transactional import read_csv
from dEclat import dEclat, dEclatControl
from dEclat.Rules import rulesInduction, InductionControl
import argparse
from datetime import datetime

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="What test to run: [normal, rules, sort, matrix, both]")

    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    if args.test == "normal":
        start = datetime.now()
        # load data in transactional format
        db = read_csv("./data/mushrooms.csv")

        # mine frequent itemsets
        DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10)
        frequentItemsets = dEclat(db, DE_params)
        end = datetime.now()
        print(f"dEclat took {(end - start).seconds} seconds")

    elif args.test == "normal":
        start = datetime.now()

        # load data in transactional format
        db = read_csv("./data/mushrooms.csv")

        # mine frequent itemsets
        DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10)
        frequentItemsets = dEclat(db, DE_params)

        # induce rules from frequent itemsets
        RI_params = InductionControl(confidence=0.5)
        ruleset = rulesInduction(frequentItemsets, db, RI_params)

        end = datetime.now()
        print(f"dEclat with rules took {(end - start).seconds} seconds")

    elif args.test == "sort":
        start = datetime.now()

        # load data in transactional format
        db = read_csv("./data/mushrooms.csv")

        # mine frequent itemsets
        DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10, sort=True)
        frequentItemsets = dEclat(db, DE_params)

        end = datetime.now()
        print(f"dEclat with sorting took {(end - start).seconds} seconds")

    elif args.test == "matrix":
        start = datetime.now()

        # load data in transactional format
        db = read_csv("./data/mushrooms.csv")

        # mine frequent itemsets
        DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10, use_matrix=True)
        frequentItemsets = dEclat(db, DE_params)

        end = datetime.now()
        print(f"dEclat with matrix took {(end - start).seconds} seconds")

    elif args.test == "both":
        start = datetime.now()

        # load data in transactional format
        db = read_csv("./data/mushrooms.csv")

        # mine frequent itemsets
        DE_params = dEclatControl(support=0.5,minlen=1, maxlen=10, sort=True, use_matrix=True)
        frequentItemsets = dEclat(db, DE_params)

        end = datetime.now()
        print(f"dEclat with both optimizations took {(end - start).seconds} seconds")
    
    else:
        print("Unknown argument, exiting...")


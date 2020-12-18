from Transactional import read_csv
from dEclat import dEclat, dEclatControl

if __name__ == "__main__":
    db = read_csv("./data/mushrooms.csv")
    print(db)
    rules = dEclat(db, dEclatControl(0.5, 1, 10))

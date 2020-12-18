from Transactional import read_csv
from dEclat import dEclat, dEclatControl

if __name__ == "__main__":
    db = read_csv("./data/test.csv")
    print(db)
    rules = dEclat(db, dEclatControl(support=0.5,minlen=1, maxlen=10))

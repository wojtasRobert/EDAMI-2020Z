import pandas as pd
from Transactional.Database import Item, Transaction, TransactionalDatabase

def read_csv(filename,):
    df = pd.read_csv(filename, na_values="?")
    
    items = []
    transactions = []

    items_map = {}
    id_counter = 1

    for (column_name, column_data) in df.iteritems():
        unique_values = column_data.unique()
        for uv in unique_values:
            if not pd.isna(uv):
                item_name = f"{column_name}={uv}"
                new_item = Item(id_counter, item_name)
                items.append(new_item)
                items_map[item_name] = new_item
                id_counter += 1

    for idx, data in df.iterrows():
        itemset = Transaction(idx+1)
        for key, value in data.to_dict().items():
            if not pd.isna(value):
                item_name = f"{key}={value}"
                itemset.push(items_map[item_name])
        transactions.append(itemset)
        
    return TransactionalDatabase(df, items, transactions)
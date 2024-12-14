import csv
import os
from collections import defaultdict
import pickle

file  = os.environ.get("FILE", "./files/data.csv")

with open(file) as f:
    reader = csv.reader(f)
    terms = [" ".join(row) for row in reader]

prifixs = defaultdict(list)

for term in terms:
    name = term.lower()
    for ch in range(1, len(name)+1):
        prefix = name[:ch]
        prifixs[prefix].append(name)
print(prifixs)

opFile = open('./processData/namesData.pkl','ab')
pickle.dump(prifixs,opFile)
opFile.close()

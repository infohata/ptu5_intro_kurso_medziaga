# EPIC FAIL
import pickle

with open("Naujas/kates.pkl", "rb") as failas:
    kates = pickle.load(failas)

for kate in kates:
# CRASH
    print(kate)

# delete spcaes before a comma, period, 'contradiction' and 'entailment'.

with open("data/DATASET_NAME.tsv", "r") as f:
    s = f.read()
s = s.replace(" ,", ",")
s = s.replace(" .", ".")
s = s.replace(" entailment", "entailment")
s = s.replace(" contradiction", "contradiction")
s = s.replace(" neutral", "neutral")
s = s.replace(" ?", "?")

with open("data/DATASET_NAME.tsv.tsv", "w") as f:
    f.write(s)

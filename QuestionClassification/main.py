from GetData import TDIUC
from DistilBERT import DistilBERT

tdiuc = TDIUC()
tdiuc, id2label, label2id = tdiuc.get_tdiuc()

distilbert = DistilBERT(id2label, label2id)

tokenized_tdiuc = distilbert.tokenize(tdiuc)
distilbert.train(tokenized_tdiuc)

print(distilbert.predict(tokenized_tdiuc))
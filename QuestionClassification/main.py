from GetData import TDIUC

tdiuc = TDIUC()
tdiuc, id2label, label2id = tdiuc.get_tdiuc()

print(id2label)
print(label2id)
print(tdiuc["test"][0])
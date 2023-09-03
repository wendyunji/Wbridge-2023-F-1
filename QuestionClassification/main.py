from GetData import TDIUC

tdiuc = TDIUC().get_tdiuc()
print(tdiuc['test'][0])
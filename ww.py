from geode import *
import numpy as np
from pprint import pprint
from time import *
## read expression data
begin_time = time()
mat = []
genes = []
with open ('111(1).csv') as f:
	next(f)
	for line in f:
		sl = line.strip().split('\t')
		gene = sl[0]
		row = list(map(float, sl[1:]))
		genes.append(gene)
		mat.append(row)
mat = np.array(mat)
# mat = np.concatenate(mat, axis=0)
col_labels = ['1','1','1','2','2','2']
y = [52,63]
# for i in range(0,2):
#     for x in range(0, y[i]):
#         col_labels.append(str(i+1))
# print(col_labels)
## compute characteristic direction
# chdir_res = chdir(mat, col_labels, genes, calculate_sig=True, nnull=31032)
chdir_res = chdir(mat, col_labels, genes, calculate_sig=True, nnull=31000)
pprint(chdir_res)
import pandas as pd
df = pd.DataFrame(chdir_res)
df.to_csv("severity_mod_CD1.csv",sep=',',header=False,index=False)
# perform PAEA gene-set enrichment analysis
# paea_res = paea_wrapper(chdir_res, 'GeneOntology_BP.gmt')
# # look at the top enriched GO terms
# pprint(paea_res[0:10])

end_time = time()
run_time = end_time-begin_time
print ('该循环程序运行时间：',run_time)

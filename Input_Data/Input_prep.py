import os

import pandas as pd
import numpy as np

os.chdir('path to your input files')

# read your CNV and clinical data as input files

CNV_file = os.path.join('CNV_Input.csv')
Clinical = os.path.join('clinical_labels.xlsx')
cnv_gene = pd.read_csv(CNV_file, index_col=0)
Clinical = pd.read_excel(Clinical, index_col=0)

# Load the list of NCA selected gene list
NCA_gene_file = os.path.join('..\NCA_Outputs','cnv_sel_features_211genes.xlsx')
nca_genes = pd.read_excel(NCA_gene_file, index_col=0)

# format files
common = set.intersection(set(cnv_gene.columns), set(nca_genes.columns))
df1= cnv_gene.loc[:, cnv_gene.columns.isin(common)]
df1.shape

# rearrange column index
sequence = list(nca_genes.columns.values)
df2 = df1.reindex(columns=sequence)

#  log2 transform CNV values if not already done
dfx = df2 + 1
dfx2 =np.log2(dfx)

# Combine both input dataframes into one df
df_Comb= pd.concat([dfx2, Clinical], axis =1)

# output files
CNV_out_file = os.path.join('newinput.csv')

df_Comb.to_csv(CNV_out_file,)


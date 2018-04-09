import re
import pandas as pd
import numpy as np
from io import StringIO

infile = 'TAIR10_functional_descriptions.txt'
outfile = "A12_taskA_out.csv"
with open(infile, 'r') as myfile:
    text = myfile.read()

results = re.sub('.*?(^AT\dG\d+\.\d+|IPR\d+|$).*?', r'\1,',text, 0, re.M)
results_io = StringIO(results)

df = pd.read_csv(results_io, names= range(15), sep=",", skiprows = 1, error_bad_lines = False) # force column count, skip header, and ignore any lines that contain more than the column limit

df.columns = ['Transcript ID', 'IPR1', 'IPR2', 'IPR3', 'IPR4', 'IPR5', 'IPR6', 'IPR7', "IPR8", "IPR9", "IPR10", "IPR11", "IPR12", "IPR13", "IPR14"] # force column names

annots = df.melt(id_vars = 'Transcript ID', value_name='IPR Term')
annots = annots.drop('variable', axis=1)
annots = annots.dropna()

annots.to_csv(outfile, sep = ',', index=False)

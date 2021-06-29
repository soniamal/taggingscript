import pandas as pd
import os
import unicodecsv 
import json


#setting up connections to input/output a file 
df = pd.read_csv("C:\\Users\\206582373\\hello\\source\\Azure_Resource_Groups_with_Tags.csv")
our_output = ("C:\\Users\\206582373\\hello\\outputifles\\Azure_Resource_Groups_Final_Tags.csv")
outdir = "outputfiles"
output_path = os.path.join(outdir, our_output)


#Separating tags logic 
for index, row in df.iterrows():
    tagging = json.loads(row['TAGS'])
    for key in tagging:
        tag = tagging[key]
        tag = tag.lower()
        key = key.lower()
        if key not in df:
            df[key] = None
            df.at[index, key] = tag
        else:
            df.at[index, key] = tag

df.to_csv(our_output, index = False)







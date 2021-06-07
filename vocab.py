import pandas as pd 
import json

import urllib.request
# url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR-JIrFA9aTC0VdHkj0HAj2zVHxQEIxiuGL7dcEpa1jdXtM96no_VxqktxM3Q3T0-kqPRTppfw81d8Q/pub?gid=1060194856&single=true&output=csv'
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQoAtLwbsZ0ifBaMqrM79UEY2JjlifQ7Hwl-x-mD9PnnO1A9CjEobaPrLnr4ZATUiZ086l3jeJzr7uW/pub?gid=789062962&single=true&output=csv'
data = urllib.request.urlretrieve(url)
filepath = data[0]

# filepath = "C:/Users/Lenovo/AppData/Local/Temp/tmpriifmle_"

print(filepath)

df = pd.read_csv(filepath)

result = [
            {abj: 
                    [
                        {"indication": word.strip()} for word in df[abj] if str(word) != 'nan'
                    ]
            } for abj in df.columns                                                  
        ]

outfile = 'vocab.json'
with open(outfile, 'w') as f:
    json.dump(result, f, indent=4)
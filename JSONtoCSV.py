from pandas import DataFrame, read_csv
import pandas as pd
from pandas.io.json import json_normalize
import json
file = "/Users/localuser/Desktop/DataExp/InputsAnalysis/UploadedData/InputsWithoutInternal.csv" #Input filename
df = pd.read_csv(file)
dflist = []
datset = dict()
for i in df.index:
    data = json.loads(df['INPUTS_JSON'][i])
    data['fpsquence'] = df['ID'][i]
    data['ClientID'] = df['ID1']
    data['createdDate'] = df['ID']
    json_normalize(data)
    for key in data.keys():
        if key in datset:
            datset[key].append(data[key])
        else:
            values = []
            values.append(data[key])
            print(data[key])
            datset[key] = values

print(datset.keys())
dataframe = pd.DataFrame({ key:pd.Series(value) for key, value in datset.items() })
dataframe.to_csv("/Users/localuser/Desktop/DataExp/InputsAnalysis/UploadedData/OutputErrorsInputs.csv", encoding='utf-8', index=False) #output filename

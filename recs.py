import json 

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def get_vocab(): 
    vocabfile = 'vocab.json'
    with open(vocabfile) as f: 
        file = json.load(f)

    vocab = []
    for i in range(len(file)):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key = alphabet[i]

        obj2 = file[i][key]

        vocab += [ obj2[i]["indication"] for i in range(len(obj2))]

    # print(vocab)

    return vocab 

def get_target(id_req, flow):
    filename = 'fix-fda-otc.csv'
    df = pd.read_csv(filename)

    if flow:
        data = list(df[~df['label_id'].isin([id_req])]['indications_and_usage'].values)
        id_data = {i: id for i, id in enumerate(list(df[~df['label_id'].isin([id_req])]['label_id'].values))}
        target = list(df[df['label_id']==id_req]['indications_and_usage'].values)

    else:  
        data = list(df['indications_and_usage'].values)
        id_data = {i: id for i, id in enumerate(list(df['label_id'].values))}
        target = id_req.split(',')

    return df, data, id_data, target 

def recommend(id_req, flow): 
    df, data, id_data, target = get_target(id_req, flow)
    
    vocab = get_vocab()
    cv = CountVectorizer(binary=True)
    cv.fit(vocab)

    data_vec = cv.transform(data).toarray()
    target_vec = cv.transform(target).toarray()

    if flow:
        n = 500 
    else:
        n = 501
    
    top = 10 

    result = {}
    for i in range(n-1): 
        ps = precision_score(target_vec[0], data_vec[i], average='binary', zero_division=0)
        if ps > 0: 
            result[id_data[i]] = ps 
  
    result_id = sorted(result, key=result.get, reverse=True)
    
    dict_res = df[df.label_id.isin(result_id)].to_dict('records')        

    for i in range(len(dict_res)): 
        res_id = result_id[i]
        dict_res[i]['precision_score'] = result[res_id]

    return dict_res
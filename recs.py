import json 

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

        vocab += [ obj2[i][str(i)] for i in range(len(obj2))]

    # print(vocab)

    return vocab 

def cosine(a, b): 
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    return cosine_similarity(a, b)

def recommend(upc_req): 
    filename = 'medy-sample-dataset.csv'
    df = pd.read_csv(filename)
    
    data = list(df[~df['upc'].isin([upc_req])]['indications_and_usage'].values)
    upc_data = {i: upc for i, upc in enumerate(list(df[~df['upc'].isin([upc_req])]['upc'].values))}
    # print(upc_data)

    target = list(df[df['upc']==upc_req]['indications_and_usage'].values)
    
    # --------------------------------------------------------------------------------------------------

    vocab = get_vocab()
    cv = CountVectorizer(binary=True, vocabulary=vocab)

    # --------------------------------------------------------------------------------------------------

    data_vec = cv.transform(data).toarray()
    target_vec = cv.transform(target).toarray()

    n = 500 
    top = 10 
    result = {upc_data[i]: cosine(data_vec[i], target_vec[0])[0][0] for i in range(n-1)}
    result_id = sorted(result, key=result.get, reverse=True)[:top]

    print('target:', df[df['upc']==upc_req]['indications_and_usage'].values)
    print(df[df.upc.isin(result_id)]['indications_and_usage'].values)

    return result_id 

# recommend(upc_req)


    # print(data_vec.shape)
    # print(target_vec.shape)

    # print(data_vec[0])
    # print(target_vec[0])
    
        # top10_upc = ['12312', '321321321', '12312312', '12312312312', '321321312']

    # return top10_upc
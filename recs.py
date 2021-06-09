import json 

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def load_data(): 
    # filename = 'results.csv'
    filename = 'demo-drugs-v1-result.csv'
    df = pd.read_csv(filename)
    dict_df = df.to_dict('records')
    return df, dict_df


def get_vocab(): 
    df, dict_df = load_data()
    # vocab = {'acne': ['blackhead', 'pimple', 'whitehead'], 
    #         'cough': ['dry cough', 'sore throat', 'deep cough', 'barking cough', 'sneezing'], 
    #         'skin': ['irritation', 'itching', 'scrapes burns', 'wrinkle']
    # } 

    cats = ['acne', 'cough', 'skin']
    vocab = {}
    for cat in cats:
        cat_vocab = [] 
        for row_entities in df[df.category==cat]['entities'].values:
            list_row_entities = row_entities.split(', ') 
            cat_vocab += list_row_entities
        un_cat_vocab = list(set(cat_vocab))
        vocab[cat] = un_cat_vocab

    # print(vocab)
    return vocab 

get_vocab()

def get_data(conditions, by_id):
    filename = 'demo-drugs-v1-result.csv'
    df = pd.read_csv(filename)
    
    if by_id:
        # conditions == id 
        label_id = conditions 
        list_entities_ = df[~df['label_id'].isin([label_id])]['entities'].values
        data = [', '.join(ents.split(', ')) for ents in list_entities_]
        id_data = {i: id for i, id in enumerate(list(df[~df['label_id'].isin([label_id])]['label_id'].values))}
        target = df[df.label_id==label_id]['entities'].values
    else:  
        data = list(df['entities'].values)
        id_data = {i: id for i, id in enumerate(list(df['label_id'].values))}
        target = [conditions]

    return df, data, id_data, target 

def recommend(conditions, by_id):
    df, data, id_data, target = get_data(conditions, by_id)
         
    vocab_dict = get_vocab()
    vocab_list = []
    for item in vocab_dict.items(): 
        vocab_list += item[1]

    # print(vocab_list)
    
    cv = CountVectorizer(binary=True)
    cv.fit(vocab_list)

    target_vec = cv.transform(target).toarray()
    data_vec = cv.transform(data).toarray()
    
    result = {}
    for i in range(len(data)): 
        ps = precision_score(target_vec[0], data_vec[i], average='binary', zero_division=0)
        if ps > 0:
            # print(ps) 
            result[id_data[i]] = ps 

    result_id = sorted(result, key=result.get, reverse=True)

    # print(result_id)

    dict_res = [df[df.label_id == rid].to_dict('records')[0] for rid in result_id]

    for i in range(len(dict_res)): 
        res_id = result_id[i]
        dict_res[i]['search_precision'] = result[res_id]
    
    return dict_res
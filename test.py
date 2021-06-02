import pandas as pd 

filename = 'medy-sample-dataset.csv'
df = pd.read_csv(filename).sample(2)

print(list(df['brand_name'].apply(lambda x: x.lower())))

'''
df = df.to_dict('records')

result = []
attrs = ['category', 'brand_name', 'effective_time',
         'purpose', 'indications_and_usage', 
         'active_ingredient', 'inactive_ingredient',
         'dosage_and_administration', 'warnings']

for i in range(len(df)):
    temp = {}
    temp['id'] = df[i]['label_id']
    
    for attr in attrs:
        if attr == 'id':
            temp[attr] = df[i]['label_id']
        elif attr == 'effective_time': 
            temp[attr] = df[i]['label_effective_time']
        else: 
            temp[attr] = df[i][attr]

    result.append(temp)

print(result)
'''
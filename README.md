## medy API

a simple API to support [*medy*](https://github.com/cahyaasrini/medy-api) android app prototype demo. 


#### 1. Data
The medicine products data used by this API is in `demo-drugs-v1-result.csv` file and the source is [here](https://www.kaggle.com/cahyaasrini/openfda-human-otc-drug-labels). 

#### 2. Deployment 
Running in [heroku](https://medy-api.herokuapp.com/) and [gcloud](https://medy-315402.et.r.appspot.com). 

#### 3. Usage 

3.1. Medicine list 

- Get all medicine

  name = 'all'


- Get a specific one by brand_name 

  name = 'Soothe and Cool Moisture Barrier' 
    
  ```
  https://medy-315402.et.r.appspot.com/medicine/<name> 
  ```

3.2. Medicine details by id / label_id  
    
   id = '0b8e057f-9834-4d71-8678-8475ec58e891'
   ```
   https://medy-315402.et.r.appspot.com/details/<id> 
   ```
   
3.3. Categories by alphabet 

   key = 'a' 
   ```
   https://medy-315402.et.r.appspot.com/keywords/<key> 
   ```

3.4. Conditions by category 

   cat = 'skin'
   ```
   https://medy-315402.et.r.appspot.com/conditions/<cat> 
   ```
  
3.5. Recommendations 

Recommendation code is in `recs.py`

- by a specific id 
  
   id = '0b8e057f-9834-4d71-8678-8475ec58e891'
   ```
   https://medy-315402.et.r.appspot.com/recommend1/<id> 
   ```
  
- by conditions 

   conditions = 'cough,fever' 
   ```
   https://medy-315402.et.r.appspot.com/recommend2/<conditions> 
   ```

## medy API

a simple API to support [*medy*](https://github.com/cahyaasrini/medy-api) android app prototype demo. 

#### Data
The medicine products data used for *medy* prototype demo is from [here](https://www.kaggle.com/cahyaasrini/openfda-human-otc-drug-labels). 

#### Deployment 

Running in [heroku](https://medy-api.herokuapp.com/) and [gcloud](https://medy-315402.et.r.appspot.com). 

#### Usage 

1. Medicines list 
    - Get all meds. 

      name = 'all' 
    - Get a specific one by brand_name 

      name = 'Soothe and Cool Moisture Barrier' 
    
      ```
      https://medy-315402.et.r.appspot.com/medicine/<name> 
      ```

2. Medicine details by id / label_id  
    
   id = '0b8e057f-9834-4d71-8678-8475ec58e891'
   ```
   https://medy-315402.et.r.appspot.com/details/<id> 
   ```
   
3. Categories by alphabet 

   key = 'a' 
   ```
   https://medy-315402.et.r.appspot.com/keywords/<key> 
   ```

4. Conditions by category 

   cat = 'skin'
   ```
   https://medy-315402.et.r.appspot.com/conditions/<cat> 
   ```
  
5. Recommendations by a specific id 
  
   id = '0b8e057f-9834-4d71-8678-8475ec58e891'
   ```
   https://medy-315402.et.r.appspot.com/recommend1/<id> 
   ```
  
6. Recommendations by conditions 

   conditions = 'cough,fever' 
   ```
   https://medy-315402.et.r.appspot.com/recommend2/<conditions> 
   ```

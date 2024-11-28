import json
from pyairtable import Api

# Set your Airtable base ID and personal access token
base_id = 'appa5jXM9idcmVzxP'
api_key = 'pat1QMFhEBhEDTh6S.6850f8fd92c6b5ca50b65558c8d6f97bd6fba9d968901c772cce0527bf9c0f39'

# Initialize the API connection
api = Api(api_key)

# Access tables using the new method
hearing_aids_table = api.table(base_id, 'Hearing Aids')
couplings_table = api.table(base_id, 'Couplings')
electroacoustics_table = api.table(base_id, 'Electroacoustics')
fitting_ranges_table = api.table(base_id, 'Fitting Ranges')
brands_table = api.table(base_id, 'Brands')

# Get all records from the Hearing Aids table
records = hearing_aids_table.all()

brands_record = brands_table.all()
brands = []

for brand_item in brands_record:
    field = brand_item['fields']
    brands.append(field['Name'])
    
# print(brands)

def find_all_families(brand):
    
    #what the func will return (set of all families)
    brand_families = set()
    
    for record in records:
        
        #gets the brand of all hearing aids
        field = record['fields']
        brand_id = field['Brand'][0]
        brand_record = brands_table.get(brand_id)
        
        #checks if brand is same as selected brand
        if brand_record['fields']['Name'] == brand:
            brand_families.add(field['Family'])
            
    return brand_families      
            
# print(find_all_families(brands[5]))

def find_all_models(family):
    
    #what the func will return (set of all models)
    family_models = set()
    
    for record in records:
        
        field = record['fields']
        
        if field['Family'] == family:
            family_models.add(field['Model'])
            
    return family_models
        
# print(find_all_models('Moment'))

def find_all_tech_lvls(family, model):
    
    tech_lvls = set()
    
    for record in records:
        field = record['fields']
        
        try:
            if field['Model'] == model and field['Family'] == family:
                tech_lvls.add(field['Technology Level'])
        except:
            return 'no tech levels'
                
    return tech_lvls

# print(find_all_tech_lvls('Moment', 'CIC'))

def find():
    print('hello, this is how you can find your hearing aid!\n')
    
    print('Hearing Aid Brands:')
    for brand in brands:
        print('- ' + brand)
        
    user_brand = input('\nplease select your brand, please type exactly as it is: ')
    
    print('\nsearching families...\n')
    
    poss_families = find_all_families(user_brand)
    
    print('Possible Families:')
    for familiy in poss_families:
        print('- ' + familiy)
        
    user_family = input('\nplease select your family, please type exactly as it is: ')
    
    print('\nsearching models...\n')
    
    poss_models = find_all_models(user_family)
    
    print('Possible Models:')
    for model in poss_models:
        print('- ' + model)

    user_model = input('\nplease select your model, please type exactly as it is: ')
    
    print('\nsearching technology levels...\n')
    
    poss_tech_lvls = find_all_tech_lvls(user_family, user_model)
    user_lvl = ''
    
    if isinstance(poss_tech_lvls, str):
        print('no technology levels found')
    else:
        print('Possible Technology Levels')
        for level in  poss_tech_lvls:
            print('- ' + level)
            
        user_lvl = input('\nplease select your technolgy level, please type exactly as it is: ')
        
    
    print(f'\nyour hearing aid is: {user_brand} {user_family} {user_model} {user_lvl}')
            
    
find()

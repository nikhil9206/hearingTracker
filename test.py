import json
from pyairtable import Api

# Set your Airtable base ID and personal access token
base_id = 'appa5jXM9idcmVzxP'
api_key = 'pat1QMFhEBhEDTh6S.6850f8fd92c6b5ca50b65558c8d6f97bd6fba9d968901c772cce0527bf9c0f39'

# Initialize the API connection
api = Api(api_key)

# Access tables using the new method
hearing_aids_table = api.table(base_id, 'Hearing Aids')
couplings_table = api.table(base_id, 'Receivers')  # The table containing receiver data
electroacoustics_table = api.table(base_id, 'Electroacoustics')  # Electroacoustics table
fitting_ranges_table = api.table(base_id, 'Fitting Ranges')  # Fitting ranges table

# Get all records from the Hearing Aids table
records = hearing_aids_table.all()

for record in records:
    fields = record['fields']
    
    # For Receivers
    try:
        if 'Receivers' in fields:
            print("Receivers:")
            for receiver_id in fields['Receivers']:
                receiver_record = couplings_table.get(receiver_id)
                receiver_name = receiver_record['fields'].get('Name', 'No Name')
                print(f" - {receiver_name}")
    except Exception as e:
        print(f"Error fetching receiver data: {e}")
    
    # For Electroacoustics
    try:
        if 'Electroacoustics' in fields:
            print("Electroacoustics:")
            for electroacoustic_id in fields['Electroacoustics']:
                electroacoustic_record = electroacoustics_table.get(electroacoustic_id)
                electroacoustic_name = electroacoustic_record['fields'].get('Profile', 'No Name')
                print(f" - {electroacoustic_name}")
    except Exception as e:
        print(f"Error fetching electroacoustics data: {e}")
    
    # For Fitting Ranges
    try:
        if 'Fitting Ranges' in fields:
            print("Fitting Ranges:")
            for fitting_range_id in fields['Fitting Ranges']:
                fitting_range_record = fitting_ranges_table.get(fitting_range_id)
                fitting_range_name = fitting_range_record['fields'].get('Fitting Range', 'No Name')
                print(f" - {fitting_range_name}")
    except Exception as e:
    print(f"Error fetching fitting ranges data: {e}")
    
    print("\n")
    
    
    
#import json
# from pyairtable import Api

# # Set your Airtable base ID and personal access token
# base_id = 'appa5jXM9idcmVzxP'
# api_key = 'pat1QMFhEBhEDTh6S.6850f8fd92c6b5ca50b65558c8d6f97bd6fba9d968901c772cce0527bf9c0f39'

# # Initialize the API connection
# api = Api(api_key)

# # Access tables using the new method
# hearing_aids_table = api.table(base_id, 'Hearing Aids')
# couplings_table = api.table(base_id, 'Couplings')
# electroacoustics_table = api.table(base_id, 'Electroacoustics')
# fitting_ranges_table = api.table(base_id, 'Fitting Ranges')

# # Get all records from the Hearing Aids table
# records = hearing_aids_table.all()

# # Function to get human-readable names from linked record IDs
# def get_linked_record_names(table, ids):
#     if not ids:
#         return []
#     names = []
#     for record_id in ids:
#         record = table.get(record_id)
#         # Assuming there's a "Name" field in the linked records
#         names.append(record['fields'].get('Name', record_id))   
#     return names

# # Loop through records and replace linked record IDs with actual data
# for record in records:
#     fields = record['fields']

#     # Replace Couplings IDs with names
#     if 'Couplings' in fields:
#         fields['Couplings'] = get_linked_record_names(couplings_table, fields['Couplings'])

#     # Replace Electroacoustics IDs with names
#     if 'Electroacoustics' in fields:
#         fields['Electroacoustics'] = get_linked_record_names(electroacoustics_table, fields['Electroacoustics'])
#     else:
#         print('electro isnt')

#     # Replace Fitting Ranges IDs with names
#     if 'Fitting Ranges' in fields:
#         fields['Fitting Ranges'] = get_linked_record_names(fitting_ranges_table, fields['Fitting Ranges'])
#     else:
#         print('fitting isnt')

# # Write the updated records with human-readable values to 'file.txt'
# with open('file.txt', 'w') as file:
#     json.dump(records, file, indent=4)
# print("Data with human-readable values has been written to 'file.txt'.")}
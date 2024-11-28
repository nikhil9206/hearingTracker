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
    
    try:
        for fitting_range_id in fields['Fitting Ranges']:
                fitting_range_record = fitting_ranges_table.get(fitting_range_id)
                fitting_range_name = fitting_range_record['fields'].get('Fitting Range', 'No Name')
                fitting_range_125l = fitting_range_record['fields'].get('125 Low', 'No Name')
                fitting_range_125h = fitting_range_record['fields'].get('125 High', 'No Name')
                fitting_range_250l = fitting_range_record['fields'].get('250 Low', 'No Name')
                fitting_range_250h = fitting_range_record['fields'].get('250 High', 'No Name')
                fitting_range_500l = fitting_range_record['fields'].get('500 Low', 'No Name')
                fitting_range_500h = fitting_range_record['fields'].get('500 High', 'No Name')
                fitting_range_1000l = fitting_range_record['fields'].get('1,000 Low', 'No Name')
                fitting_range_1000h = fitting_range_record['fields'].get('1,000 High', 'No Name')
                fitting_range_2000l = fitting_range_record['fields'].get('2,000 Low', 'No Name')
                fitting_range_2000h = fitting_range_record['fields'].get('2,000 High', 'No Name')
                fitting_range_4000l = fitting_range_record['fields'].get('4,000 Low', 'No Name')
                fitting_range_4000h = fitting_range_record['fields'].get('4,000 High', 'No Name')
                fitting_range_8000l = fitting_range_record['fields'].get('8,000 Low', 'No Name')
                fitting_range_8000h = fitting_range_record['fields'].get('8,000 High', 'No Name')
                print({fitting_range_name})
                print(f" - {fitting_range_125l}")
                print(f" - {fitting_range_125h}")
                print(f" - {fitting_range_250l}")
                print(f" - {fitting_range_250h}")
                print(f" - {fitting_range_500l}")
                print(f" - {fitting_range_500h}")
                print(f" - {fitting_range_1000l}")
                print(f" - {fitting_range_1000h}")
                print(f" - {fitting_range_2000l}")
                print(f" - {fitting_range_2000h}")
                print(f" - {fitting_range_4000l}")
                print(f" - {fitting_range_4000h}")
                print(f" - {fitting_range_8000l}")
                print(f" - {fitting_range_8000h}")
    except:
        print('none')
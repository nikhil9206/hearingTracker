import json
from pyairtable import Api
import matplotlib.pyplot as plt
import numpy as np

# Set your Airtable base ID and personal access token
base_id = 'appa5jXM9idcmVzxP'
api_key = 'pat1QMFhEBhEDTh6S.6850f8fd92c6b5ca50b65558c8d6f97bd6fba9d968901c772cce0527bf9c0f39'

# Initialize the API connection
api = Api(api_key)

# Access tables using the new method
hearing_aids_table = api.table(base_id, 'Hearing Aids')
reciever_table = api.table(base_id, 'Receivers')  # The table containing receiver data
electroacoustics_table = api.table(base_id, 'Electroacoustics')  # Electroacoustics table
fitting_ranges_table = api.table(base_id, 'Fitting Ranges')  # Fitting ranges table
couplings_table = api.table(base_id, 'Couplings') # Couplings table

#fitting range table
fitting_ranges = fitting_ranges_table.all()


for record in fitting_ranges:    
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Hearing Level in db (HL)")
    
    field = record['fields']
    
    #actual fitting range data points
    
    try:
        high_y = np.array([field['125 High'], field['250 High'], field['500 High'], field['1,000 High'], field['2,000 High'], field['4,000 High'], field['8,000 High']])
        low_y = np.array([field['125 Low'], field['250 Low'], field['500 Low'], field['1,000 Low'], field['2,000 Low'], field['4,000 Low'], field['8,000 Low']])
    except:
        high_y = np.array([0, field['250 High'], field['500 High'], field['1,000 High'], field['2,000 High'], field['4,000 High'], field['8,000 High']])
        low_y = np.array([0, field['250 Low'], field['500 Low'], field['1,000 Low'], field['2,000 Low'], field['4,000 Low'], field['8,000 Low']])
        
    #placeholder x-values
    x = np.array([1,2,3,4,5,6,7])
    
    
    #hearing aid retriving
    hearing_aid_id = field['Hearing Aid'][0]
    hearing_aid_record = hearing_aids_table.get(hearing_aid_id)
    hearing_aid = hearing_aid_record['fields']['Hearing Aid']
    
    #reciever retriving
    try:
        reciever_id = field['Receiver'][0]
        reciever_record = reciever_table.get(reciever_id)
        reciever = reciever_record['fields']['Name']
    except:
        receiver = ''
    
    #coupling retriving
    try:
        coupling_id = field['Receiver'][0]
        coupling_record = couplings_table.get(coupling_id)
        coupling = coupling_record['fields']['Coupling']
    except:
        coupling = ''
        
    #complete name
    full_name = f'{hearing_aid} {reciever} {coupling}'
    
    plt.title(full_name)
        
    plt.plot(x, low_y)
    plt.plot(x, high_y)
    plt.xticks(np.arange(0, 8, step=1), labels=['', '125', '250', '500', '1K', '2K', '4K', '8K'])
    plt.fill_between(x, low_y, high_y, color='blue', alpha=0.7)
    plt.savefig(f"plots/{full_name}.jpg")
    
    plt.clf()
    
    
    
    
    
        
# low_y = np.array([0, 0, 0, 0, 0, 0, 0])
# high_y = np.array([45, 45, 55, 70, 85, 85, 85])
# x = np.array([1,2,3,4,5,6,7])


# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Hearing Level in db (HL)")
# plt.title('')
# plt.plot(x, low_y)
# plt.plot(x, high_y)
# plt.xticks(np.arange(0, 8, step=1), labels=['', '125', '250', '500', '1K', '2K', '4K', '8K'])
# plt.fill_between(x, low_y, high_y, color='blue', alpha=0.7)
# plt.savefig("plots/output.jpg")
# plt.show()
# plt.clf()
# plt.show()


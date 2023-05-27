from firebase_admin import firestore, credentials, initialize_app
import pandas as pd
from datetime import datetime
import time

cred = credentials.Certificate('tcc-mental-health-credentials.json')
initialize_app(cred)
db = firestore.client()
users_ref = db.collection(u'Users')
forms_ref = db.collection(u'Forms')
trackings_ref = db.collection(u'Trackings')

user_forms = []
user_data = pd.read_csv('formated_data.csv')
user_data['Dob'].fillna('01/01/1970', inplace=True)
users = {}
forms = {}

docs = forms_ref.get()
for doc in docs:
    forms[doc.to_dict()['disorder']] = doc.id

for index in range(0, len(user_data['Stamp'])):
    update_time, user_ref = users_ref.add({
        u'DoB': datetime.fromtimestamp(time.mktime(datetime.strptime(user_data['Dob'][index], '%d/%m/%Y').timetuple())),
        u'Children': int(user_data['Children'][index]),
        u'Age': int(user_data['Age'][index]),
        u'University': str(user_data['University'][index]),
        u'Email': user_data['Email'][index],
        u'Gender': user_data['Gender'][index],
        u'Course': user_data['Course'][index],
        u'Ocupation': user_data['Ocupation'][index],
        u'Grad_Period': int(user_data['Grad_Period'][index]),
        u'Marital_Status': user_data['Marital_Status'][index],
        u'Name': '',
        u'Surname': '',
        u'Terms': user_data['Terms'][index],
        u'UserForms': {
            u'Stamp': datetime.fromtimestamp(time.mktime(datetime.strptime(user_data['Stamp'][index], '%d/%m/%Y %H:%M:%S').timetuple())),
            u'Forms': [
                {
                    u'formId': forms['S1'],
                    u'answer': int(user_data['S1'][index])
                },
                {
                    u'formId': forms['A2'],
                    u'answer':int( user_data['A2'][index])
                },
                {
                    u'formId': forms['D3'],
                    u'answer':int( user_data['D3'][index])
                },
                {
                    u'formId': forms['A4'],
                    u'answer':int( user_data['A4'][index])
                },
                {
                    u'formId': forms['D5'],
                    u'answer':int( user_data['D5'][index])
                },
                {
                    u'formId': forms['S6'],
                    u'answer':int( user_data['S6'][index])
                },
                {
                    u'formId': forms['A7'],
                    u'answer':int( user_data['A7'][index])
                },
                {
                    u'formId': forms['S8'],
                    u'answer':int( user_data['S8'][index])
                },
                {
                    u'formId': forms['A9'],
                    u'answer':int( user_data['A9'][index])
                },
                {
                    u'formId': forms['D10'],
                    u'answer': int(user_data['D10'][index])
                },
                {
                    u'formId': forms['S11'],
                    u'answer': int(user_data['S11'][index])
                },
                {
                    u'formId': forms['S12'],
                    u'answer': int(user_data['S12'][index])
                },
                {
                    u'formId': forms['D13'],
                    u'answer': int(user_data['D13'][index])
                },
                {
                    u'formId': forms['S14'],
                    u'answer': int(user_data['S14'][index])
                },
                {
                    u'formId': forms['A15'],
                    u'answer': int(user_data['A15'][index])
                },
                {
                    u'formId': forms['D16'],
                    u'answer': int(user_data['D16'][index])
                },
                {
                    u'formId': forms['D17'],
                    u'answer': int(user_data['D17'][index])
                },
                {
                    u'formId': forms['S18'],
                    u'answer': int(user_data['S18'][index])
                },
                {
                    u'formId': forms['A19'],
                    u'answer': int(user_data['A19'][index])
                },
                {
                    u'formId': forms['A20'],
                    u'answer': int(user_data['A20'][index])
                },
                {
                    u'formId': forms['D21'],
                    u'answer': int(user_data['D21'][index])
                }
            ]
            
            
        }
    })
    users[index] = user_ref.id





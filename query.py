from firebase_admin import firestore, credentials, initialize_app
import pandas as pd
from datetime import datetime
import time

cred = credentials.Certificate('tcc-mental-health-credentials.json')
initialize_app(cred)
db = firestore.client()
user_forms_ref = db.collection(u'UserForms')
users_ref = db.collection(u'Users')

users_doc = users_ref.get()
users_id = []
for doc in users_doc:
    users_id.append(doc.id)


for i in range(0, len(users_id), 10):
    user_forms_doc = user_forms_ref.where('userId', 'not-in', users_id[i:i+10]).stream()


for doc in user_forms_doc:
    print(f'{doc.id} => {doc.to_dict()}')






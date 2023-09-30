import firebase_admin
from firebase_admin import credentials,db

# Authenticate to firebase
cred = credentials.Certificate("./Tools/sql/Firebase/focusflow.json")
firebase_admin.initialize_app(cred)

# Creating reference to rood node
ref = db.reference('/users/yWA8ifPBJjbNodsdijza')

# Retrieving data from root node 
ref.get()


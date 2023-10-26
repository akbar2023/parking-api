import firebase_admin
from firebase_admin import credentials
from configs.firebase_config_example import  firebaseConfig
import pyrebase

if not firebase_admin._apps:
  cred = credentials.Certificate("configs/parkingapi-f5d07-firebase-adminsdk-vgm7u-d012307c45.json")
  firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
authSession = firebase.auth()
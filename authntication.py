import pyrebase
from pwinput import pwinput

firebaseConfig = {
 'apiKey': "AIzaSyBoIeeUmfqb8mLASLwDLOO3dDYj0mqqMeY",
  'authDomain': "auth-a7d56.firebaseapp.com",
  "databaseURL": "https://auth-a7d56-default-rtdb.firebaseio.com/",
  'projectId': "auth-a7d56", 
  'storageBucket': "auth-a7d56.firebasestorage.app",
  'messagingSenderId': "317934736907",
  'appId': "1:317934736907:web:c736df6c912cbd916bd90e",
  'measurementId': "G-2KBS03T5BJ"}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login():
    ask=input('Are you a new user?[yes/no]: ')
    if ask =='yes':
        create_user()
    else:
        email=input('Enter your email: ')
        password=pwinput("Enter password: ")
        try:
            login=auth.sign_in_with_email_and_password(email, password)
            print('Successfull')
        except:
            print("Invalid email or password") 
            while
   
    
def create_user():
    email=input('Enter your email: ')
    password=pwinput("Enter password: ")
    try:
        auth.create_user_with_email_and_password(email, password)
        print('Successfull')
    except: 
        print('User already exists')
        q=input('Go to log in?[yes/no]: ')
        if q=='yes':
            login()
    return email, password
login()



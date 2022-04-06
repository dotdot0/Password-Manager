import email
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDawwJkFB-1qLskM503K8C-T3pBLXqDheg",
    'authDomain': "python-aaf66.firebaseapp.com",
    'databaseURL':"https://python-aaf66-default-rtdb.firebaseio.com/",
    'projectId': "python-aaf66",
    'storageBucket': "python-aaf66.appspot.com",
    'messagingSenderId': "1039266094652",
    'appId': "1:1039266094652:web:5d3a0a2a040c5ad241ad39",
    'measurementId': "G-XG2XRX3KSD"
}

firebase = pyrebase.initialize_app(firebaseConfig)

loginstatus = None

db = firebase.database()
auth = firebase.auth()
def stringmod(s):
    for i in range(0, len(s)+1):
        if s[i] == '@':
            return s[0:i]



print('1.Log In: ')
print('2.Sign Up: ')

def login():
    email1 = input('E-Mail: ')
    passwd = input('Password: ')

    try:
        user = auth.sign_in_with_email_and_password(email1, passwd)
        print('Successfully Logged In!')
        print('----------------------------------------------------')
        loginstatus = True

    except:
        print('Invalid Email or Password!')
        print('----------------------------------------------------')
        loginstatus = False

    if loginstatus == True:

        while True: 

            print('1 --> Add New Password')
            print('2 --> Delete Password')
            print('3 --> Update Password')
            print('4 --> Find Password')
            print('5 --> Exit')

            ch = int(input(('Enter Your Choice(1-5): ')))

            #Add Password

            if ch == 1:
                websitename = input('Website Name: ')
                username = input('User Name: ')
                email = input('E-Mail: ')
                passw = input('Password: ')
                data = {
                    'website' : websitename,
                    'user': username,
                    'password':passw,
                    'email': email   
                }
                s = stringmod(email1)
                db.child('websites').child(s).child(websitename).set(data)
                print('Password Added!')
                print('----------------------------------------------------')
            
            #Delete Password

            elif ch == 2:
                websitename = input('Website Name: ')
                s = stringmod(email1)
                db.child('websites').child(s).child(websitename).remove()
                print('Password Deleted!')
                print('----------------------------------------------------')

            #Update Password

            elif ch == 3:
                websitename = input('Website Name: ')
                password = input('Enter Updated Password: ')
                s = stringmod(email1)
                db.child('websites').child(s).child(websitename).update({'password': password})
                data = db.child('websites').child(s).child(websitename).get()
                print('New Password:',data.val()['password'])
                print('----------------------------------------------------')
            
            #Display Password

            elif ch == 4:
                websitename = input('Website Name: ')
                s = stringmod(email1)
                try:
                    data = db.child('websites').child(s).child(websitename).get()
                    print('Password:',data.val()['password'])
                    print('UserName:',data.val()['user'])
                    print('----------------------------------------------------')
                except:
                    print('No Password Stored!')
        
            elif ch == 5:
                break


def Signup():
    email = input('E-Mail: ')
    passwd = input('Password: ')
    try:
        auth.create_user_with_email_and_password(email, passwd)
        print('Account Created!')
        print('----------------------------------------------------')
        print('Login To Your Account: ')
        print('----------------------------------------------------')
        login()
    except:
        print('User already exist!')
        print('Login To Your Account!')
        login()

ch = int(input('1 --> Login || 2 --> Create New Account :-- '))

if ch == 1:
    print('----Login----')
    print('----------------------------------------------------')
    login()

elif ch == 2:
    print('----SignUp----')
    print('----------------------------------------------------')
    Signup()
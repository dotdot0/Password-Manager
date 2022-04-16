
import pyrebase
from fds import stringmod
from randpasw import passwGen
from cryptography.fernet import Fernet

firebaseConfig = {
    'apiKey': "**********************",
    'authDomain': "********************",
    'databaseURL':"********************",
    'projectId': "**********",
    'storageBucket': "**********",
    'messagingSenderId': "********************",
    'appId': "*************************************",
    'measurementId': "***********"
}

firebase = pyrebase.initialize_app(firebaseConfig)

#Login Status
loginstatus = [False,]



db = firebase.database()
auth = firebase.auth()

ls = []

print('1.Log In: ')
print('2.Sign Up: ')

def encrypter(password):
    key = Fernet.generate_key()
    p = password.encode()
    f_obj = Fernet(key)
    p_en=f_obj.encrypt(p)
    return p_en.decode('utf-8'),key.decode('utf-8')

#login function
def login():
    email1 = input('E-Mail: ')
    passwd = input('Password: ')
    s = stringmod(email1)

    #Getting all website name from database
    def passwordgetter():
             data = db.child('websites').child(s).get()
             if data.val() != None:
                for a in data:
                    ls.append(a.val()['website'])
                return ls

             else:
                 print('Adding...')
             
#Log In
    try:
        if passwd == 'resetpassword':
            emailreset = input('Enter your E-Mail: ')
            auth.send_password_reset_email(emailreset)
            print('Password Reset E-Mail Sent')
            print('Reset Password')
            print('Login Again!')
            login()

        else:
            user = auth.sign_in_with_email_and_password(email1, passwd)
            print('Successfully Logged In!')
            print('-'*30)

            loginstatus[0] = True

    except:
        print('Invalid Email or Password!')
        print('-'*30)

        loginstatus[0] = False

    if loginstatus[0] == True:

        while True: 

            print('1 --> Add New Password')
            print('2 --> Delete Password')
            print('3 --> Update Password')
            print('4 --> Find Password')
            print('5 --> All Password Stored')
            print('6 --> Generate Password And Strore It')
            print('7 --> Exit')

            ch = int(input(('Enter Your Choice(1-5): ')))

            #Add Password

            if ch == 1:
                passwordgetter()

                websitename = input('Website Name: ')
                
                #Website in database or not
                if websitename in ls:
                    print('Password for the website already strored!')
                    print('-'*30)
                    continue

                else:
                    username = input('User Name: ')
                    email = input('E-Mail: ')
                    passw = input('Password: ')
                    key = Fernet.generate_key()      
                    f_obj = Fernet(key)
                    passw_normal = passw.encode()
                    encrypt = f_obj.encrypt(passw_normal)
                    en = encrypt.decode('UTF-8')
                    key_str = key.decode('UTF-8')
                    
                    data = {
                        'website' : websitename,
                        'user': username,
                        'password':en,
                        'email': email,
                        'key': key_str 
                    }

                    db.child('websites').child(s).child(websitename).set(data)
                    print('Password Added!')
                    print('-'*30)
            
            #Delete Password

            elif ch == 2:
                passwordgetter()
                websitename = input('Website Name: ')
                if websitename in ls:

                    db.child('websites').child(s).child(websitename).remove()
                    print('Password Deleted!')
                    print('-'*30)
                
                else:
                    print('No password stored for the site!')
                    print('-'*30)
                    continue

            #Update Password

            elif ch == 3:
                passwordgetter()
                websitename = input('Website Name: ')

                if websitename in ls:

                    password = input('Enter Updated Password: ')
                    db.child('websites').child(s).child(websitename).update({'password': password})
                    data = db.child('websites').child(s).child(websitename).get()
                    print('New Password:',data.val()['password'])
                    print('-'*30)

                else: 
                    print('No password stored for the site!')
                    print('-'*30)
                    continue
            
            #Display Password

            elif ch == 4:
                websitename = input('Website Name: ')
                try:
                    data = db.child('websites').child(s).child(websitename).get()
                    #print('Password:',data.val()['password'])
                    passwor_en = data.val()['password']
                    res = bytes(passwor_en,'utf-8')
                    res_key = bytes(data.val()['key'], 'utf-8')
                    f_dec = Fernet(res_key)
                    h = f_dec.decrypt(res)
                    print('Password: ',h.decode('utf-8'))
                    print('UserName:',data.val()['user'])
                    print('-'*30)
                except:
                    print('No Password Stored!')

            #Display All Password
            
            elif ch == 5:
                data = db.child('websites').child(s).get()
                passwordgetter()
                for a in data:
                    print('Website: ',a.val()['website'])
                    print('UserName: ',a.val()['user'])
                    key_Res = a.val()['key']
                    pas_normal = a.val()['password']
                    b_key = bytes(key_Res, 'utf-8')
                    pas_b = pas_normal.encode()
                    f = Fernet(b_key)
                    pass_enc = f.decrypt(pas_b)
                    password_true = pass_enc.decode('utf-8')
                    print('Password: ',password_true)
                    print('-'*30)

            #Generate password

            elif ch == 6:
                websitename = input('Website Name: ')
                email = input('E-Mail: ')
                user = input('Username: ')
                passwd = passwGen()
                key = Fernet.generate_key()
                f_obj1 = Fernet(key)
                pass_byte= passwd.encode()
                encrpt1 = f_obj1.encrypt(pass_byte)
                en1 = encrpt1.decode('utf-8')
                kry = key.decode('utf-8')
                print('Password Generated: ', passwd)
                data = {
                    'website' : websitename,
                    'user': user,
                    'password':en1,
                    'email': email ,
                    'key' : kry
                }
                db.child('websites').child(s).child(websitename).set(data)
                print('Password Added!')
                print('-'*30)

            #Exit

            elif ch == 7:
                print('Application Closed!')
                break



def Signup():
    email = input('E-Mail: ')
    passwd = input('Password: ')

    try:
        auth.create_user_with_email_and_password(email, passwd)
        print('Account Created!')
        print('-'*30)
        print('Login To Your Account: ')
        print('-'*30)
        login()

    except:
        print('User already exist!')
        print('Login To Your Account!')
        login()

ch = int(input('1 --> Login || 2 --> Create New Account :-- '))

if ch == 1:
    print('----Login----')
    print('-'*30)

    login()

elif ch == 2:
    print('----SignUp----')
    print('-'*30)

    Signup()


from os import sep
import mysql.connector as sqlcon

db = sqlcon.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "maindatabase"
)

print('----------Welcome To Password Manager----------')
print('-----MENU-----')
print('------------------------')
print('1. Add New Password--')
print('------------------------')
print('2. Find Password For Given Site--')
print('------------------------')
print('3. Total Password Stored--')
print('------------------------')
print('4. Delete Password--')
print('------------------------')
print('5. Delete All Password--')
print('------------------------')
print('6. Display All Password')
print('------------------------')
print('7.Exit')


mycursor = db.cursor()

while True:
    #Adding New Password
    ch = int(input('Enter your choice from (1-7): '))
    if ch == 1:
        

      websitename = input('Enter the website name: ')
      username = input('Enter the username used: ')
      email = input('E-Mail: ')
      passwod = input('Password: ')
     
      #Adding data to database
      mycursor.execute("INSERT INTO Passdb (websitename, username, email, password) VALUES (%s, %s, %s, %s)",(websitename, username, email, passwod))
      db.commit()  

      myweb = (websitename,)

      mycursor.execute("SELECT websitename,username,email,password FROM Passdb WHERE websitename = %s", myweb)

      #Showing the inserted data
      for x in mycursor:
         print('WebSite: ' + x[0])
         print('E-Mail: ' + x[1])
         print('UserName: ' + x[2])
         print('Password: ' + x[3])

    elif ch == 2: 
        #Find Password
        webname = input('Enter the name of the website: ')
        mydata = (webname,)
        
        #Checking whether a website exist
        mycursor.execute("SELECT websitename FROM Passdb")

        x = mycursor.fetchall()#Returns a list with tuples of name of websites

        #Checking whether website in database or not
        if mydata in x:

            mycursor.execute("SELECT username,password FROM Passdb WHERE websitename = %s", mydata)

            for x in mycursor:
                print('UserName: ' + x[0])
                print('Password: ' + x[1])

        else:
            print('No password for the website')

    #No Password Stored       
    elif ch == 3:
        mycursor.execute("SELECT * FROM Passdb")
        
        #x --> list contaning all the data
        x = mycursor.fetchall()

        print('Number Of Password Stored: ' + str(len(x)))

    elif ch == 4:

        web_name = input('Enter the name of the website: ')
        mywebs = (web_name,)


        #Check whether website exist
        mycursor.execute("SELECT websitename FROM Passdb")
        y = mycursor.fetchall()

        if mywebs in y:

            mycursor.execute("DELETE FROM Passdb WHERE websitename = %s", mywebs)

            print('Password of Website: ', web_name, ' is deleted')

        else:
            print('Website not in database')

    elif ch == 5:

        #Delete all rows
        mycursor.execute("DELETE FROM Passdb")

        print('All passwords have been removed👍')

    elif ch == 6:

        mycursor.execute("SELECT * FROM Passdb")

        z = mycursor.fetchall()

        if len(z) == 0:
            print('No Password Are Stored')

        else:
            for s in z:
                print('Website: '  + s[0] +  '| E-Mail: ', s[1] +  '| UserName: ', s[2], '| Password: ' + s[3])

    elif ch == 7:
        ans = input('Do you want to exit(y/n): ')
        if ans == 'y':
            print('App closed!')
            break
            
        else:
            continue

    else:
        print('Invalid Input!')


#mycursor.execute("CREATE DATABASE maindatabase")

#mycursor.execute("CREATE TABLE Passdb (websitename VARCHAR(50), username VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")

#Adding Data to database 
"""mycursor.execute("INSERT INTO Passdb (websitename, username, email, password) VALUES (%s, %s, %s, %s)",(websitename, username, email, passwod))
db.commit()  

mycursor.execute("SELECT * FROM Passdb")

for x in mycursor:
    print(x)"""

#Retriving Data from database


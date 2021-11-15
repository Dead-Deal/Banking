import pickle
import random
import string
import mysql.connector


print("*"*15,"OUR BANK","*"*15)
c=""

while c != 5:
    print("\n")
    print("*"*15,"Menu:","*"*15)
    print("*"*15,"1)Deposit Money","*"*15)
    print("*"*15,"2)Withdraw money","*"*15)
    print("*"*15,"3)Show Passbook details","*"*15)
    print("*"*15,"4)Other Account Services","*"*15)
    print("*"*15,"5)Exit","*"*15)

    print()
    c = int(input("Enter your choice:"))
    print()

    if c == 4:
        print("*"*15,'1)Create account',"*"*15)
        print("*"*15,'2)Modify account',"*"*15)
        print("*"*15,'3)Delete account',"*"*15)
        print("*"*15,'4)Back',"*"*15)
        print()

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "bank")
        mycursor = mydb.cursor()
        
        sc = ''
        
        while sc != 4:
            sc = int(input('Enter your choice:'))
            print()
            if sc == 1:
                res = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = 8))

                print('THANKS FOR CHOOSING OUR BANK')
                print()
                
                nam = input('Enter your full name:')
                ad = input('Enter your address:')
                mn = int(input('Enter your mobile number:'))
                rs = int(input('Initial Deposit:'))
                no = int(input('Enter an Account number:'))
                
                
                sql = "INSERT INTO pin VALUES (%s, %s)"
                val = [res,no]
                mycursor.execute(sql,val)
                mydb.commit()
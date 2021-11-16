import pickle
import random
import string
import mysql.connector


print("*"*15,"OUR BANK","*"*15)
option_1=""

while option_1 != 5:
    print("\n")
    print("*"*15,"Menu:","*"*15)
    print("*"*15,"1)Deposit Money","*"*15)
    print("*"*15,"2)Withdraw money","*"*15)
    print("*"*15,"3)Show Passbook details","*"*15)
    print("*"*15,"4)Other Account Services","*"*15)
    print("*"*15,"5)Exit","*"*15)

    print()
    option_1 = int(input("Enter your choice:"))
    print()

    if option_1 == 4:
        option_2 = ""
        
        while option_2 != 4:
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
        
            option_2 = int(input('Enter your choice:'))
            print()

            if option_2 == 1:
                res = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = 8))

                print('THANKS FOR CHOOSING OUR BANK')
                print()
                
                nam = input('Enter your full name:')
                ad = input('Enter your address:')
                mn = int(input('Enter your mobile number:'))
                rs = int(input('Initial Deposit:'))
                no = int(input('Enter an Account number:'))
                print()
                
                mycursor.execute("SELECT Account_Number FROM info")
                result = mycursor.fetchall()
                acc_no_list = []
                for results in result:
                    for i in results:
                        acc_no_list.append(i)
                while no in acc_no_list:
                    print('Account number already registered: ')
                    no = int(input('Choose another Account number: '))
                    print()
                sql = "INSERT INTO info VALUES (%s, %s, %s, %s, %s)"
                val = [res,nam,ad,mn,no]
                mycursor.execute(sql,val)
                mydb.commit()

                pin = int(input('Enter a numeric pin/password: '))
                print()
                with open('pin_code.dat','ab') as fpin:
                    x = {res, pin}
                    pickle.dump(x,fpin)
                print('CONGRATULATIONS!, Your Account has been CRAETED')
                print()
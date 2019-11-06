import numpy as np
import cv2
import mysql.connector

trys = 5
bypass = False

canvas_accessdenied = np.zeros((600,800,3),dtype="uint8")
cv2.rectangle(canvas_accessdenied, (100, 230), (700, 370), (255,255,0), 2)
cv2.putText(canvas_accessdenied, "ACCESS DENIED", (150,320), cv2.FONT_HERSHEY_SIMPLEX, 2,(100,100,255), 5)

connection = mysql.connector.connect(host='localhost',
                                        database='py_test',
                                        user='root',
                                        password='1234')

cur = connection.cursor()
true_2 = True
trys_ = False
while trys_ is False :
    while (true_2 is True) :
        user_ = str(input('Username: '))
        cur.execute('SELECT EXISTS(SELECT * FROM pass WHERE user = ' + '\'' + user_ + '\');')
        for i in cur :
            user_check = i[0]
        if user_check == 1 :
            true_2 = False
        elif user_ == '.admin' :
            true = True
            while true is True :
                cmd = input('>>')
                if cmd == 'inc attempt' :
                    inc = int(input())
                    trys += inc
                    true = False
                    break
                elif cmd == 'bypass' :
                    bypass = True
                    true = False
                    true_2 = False
                    break
                elif cmd == 'new' :
                    new_username = input('Enter new username: ')
                    new_password = input('Enter new password: ')
                    cur.execute('insert into pass values ( ' + '\'' + new_username + '\' ,' + '\'' + new_password + '\' )')
                    connection.commit()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()

                    true = False
                    break
                elif cmd == 'exit' :
                    true = False
                    true_2 = False
                    break
                else :
                    print('Invalid Command')
            if true is False :
                continue
        else :
            print('Enter a valid username')
    if bypass is True :
        break
    while trys > 0 :
        cur.execute("select password from pass where user = " + '\'' + user_ + '\' ;')
        for i in cur :
            pass_check = i[0]
        password = str(input("Enter Password: "))
        if password == pass_check :
            trys_ = True
            break
        elif password == '.show' :
            cur.execute('select password from pass where user = ' + '\'' + user_ + '\' ')
            for i in cur :
                print(i[0])
            print()
            print()
            print()
            print()
            print()
            print()
            print()
        elif password == '.change' :
            new_pass = input('Enter the new password: ')
            cur.execute('update pass set password = \'' + new_pass + '\' where user = \'' + user_ + '\' ;' )
            connection.commit()
        else :
            print('Incorrect Password')
            trys = trys - 1
            if trys == 0 :
                print('LOCKED')
                cv2.imshow("Canvas Access Denied",canvas_accessdenied)
                cv2.waitKey(0) 
                cv2.destroyAllWindows()
                trys_ = True
                break
            else :
                print(trys,' trys left')

if trys > 0 :
    print('Welcome')


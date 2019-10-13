import numpy as np
import cv2

pw1 = '0000'
trys = 5
true = True

canvas_accessdenied = np.zeros((600,800,3),dtype="uint8")
cv2.rectangle(canvas_accessdenied, (100, 230), (700, 370), (255,255,0), 2)
cv2.putText(canvas_accessdenied, "ACCESS DENIED", (150,320), cv2.FONT_HERSHEY_SIMPLEX, 2,(100,100,255), 5)

while trys > 0 :
    password = str(input("Enter Password: "))
    if password == pw1 :
        break
    elif password == '.admin' :
        while true is True :
            cmd = input('>>')
            if cmd == 'change password' :
                pw1 = input("New Password: ")
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                break
            elif cmd == 'inc attempt' :
                inc = int(input())
                trys += inc
                break
            elif cmd == 'bypass' :
                true = False
                break
            elif cmd == 'show key' :
                print(pw1)
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                break
            else :
                print('Invalid Command')
        if true is False :
            break
        
    else :
        print('Incorrect Password')
        trys = trys - 1
        if trys == 0 :
            print('LOCKED')
            cv2.imshow("Canvas Access Denied",canvas_accessdenied)
            cv2.waitKey(0) 
            cv2.destroyAllWindows()
            break
        else :
            print(trys,' trys left')

if trys > 0 :
    print('Welcome')


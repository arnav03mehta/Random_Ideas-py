
#________________________________________________________________________________________________#

def calc(line):
    l = []
    for i in range(len(line)):
        l.append(line[i])

    if l.count('+') == 0 :
        if l.count('-') == 0 :
            if l.count('*') == 0 :
                if l.count('/') == 0 :
                        if l.count('^') == 0 :
                            print('wtf')
                        else :
                            n = l.index ('^')
                else :
                    n = l.index ('/')
            else :
                n = l.index ('*')
        else :
            n = l.index ('-')
    else :
        n = l.index ('+')

    
    b = ''
    if l[n] == '/' :
        if l.count('/') == 2 :
            for f in range((n+2),len(l)):
                b += l[f]
        else :
            for f in range((n+1),len(l)):
                b += l[f]
    else :
        for f in range((n+1),len(l)):
            b += l[f]

    a = ''
    for e in range(n):
        a += l[e]
    
    if l[n] == '+' :
        c = int(a) + int(b)
    elif l[n] == '-' :
        c = int(a) - int(b)
    elif l[n] == '*' :
        c = int(a) * int(b)
    elif l[n] == '/' :
        if l.count('/') == 1 :
            c = int(a) / int(b)
        elif l.count('/') == 2 :
            c = int(a) // int(b)
    elif l[n] == '^' :
        c = int(a) ** int(b)

    return print(c)

#________________________________________________________________________________________________#

def factorial(f) :
    no = 0
    fact = 1
    while no < f :
        no = no + 1
        fact *= no
    return fact

#________________________________________________________________________________________________#

def password(key) :
    import numpy as np
    import cv2
    import sys
    pw1 = '0000'
    trys = 5
    true = True
    canvas_accessdenied = np.zeros((600,800,3),dtype="uint8")
    cv2.rectangle(canvas_accessdenied, (100, 230), (700, 370), (255,255,0), 2)
    cv2.putText(canvas_accessdenied, "ACCESS DENIED", (150,320), cv2.FONT_HERSHEY_SIMPLEX, 2,(100,100,255), 5)

    while trys > 0 :
        password = str(input("Enter Password: "))
        if password == pw1 :
            return True
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
                    return True
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

#________________________________________________________________________________________________#


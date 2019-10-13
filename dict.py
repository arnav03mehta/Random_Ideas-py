num = int(input())
d = {}
l = []
for i in range(num) :
    name_number = (input('Enter name : '), int(input('Enter number : ')))
    l.append(name_number)
    d = dict(name_number)
print()
print()
while (True) :
    print()
    print()
    name_input =  input()
    if name_input == '.end' :
        break
    print('number : ', d[name_input])

statement = input()
statement_ = []

for i in range(len(statement)) :
    statement_.append(statement[i])

spaces = [0,len(statement_)]
for j in range(len(statement_)) :
    if statement_[j] == ' ' :
        spaces.insert(len(spaces)-1, j)

n = 1
d = {}
word_lists = []

for a in range(len(spaces)) :
    if a < (len(spaces)-1) :
        if spaces[a] == 0 :
            l_1 = statement_[spaces[a]:spaces[a+1]]
            a_1 = ''
            for e in range(len(l_1)) :
                a_1 += l_1[e]
            word_ = ('word_'+str(n), a_1)
            n += 1
            word_lists.append(word_)
        else :
            l_2 = statement_[(spaces[a]+1):spaces[a+1]]
            a_2 = ''
            for e in range(len(l_2)) :
                if l_2[e] != '.' :
                    if l_2[e] != ',' :
                        if l_2[e] != '?' :
                            a_2 += l_2[e]
            word_ = ('word_'+str(n), a_2)
            n += 1
            word_lists.append(word_)

d = dict(word_lists)
d_list = []
for q in d :
    d_list.append(d[q])

print(d_list)

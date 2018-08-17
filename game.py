from random import random

import time, os, sys, random, thread
import platform

win = 0

windws = (platform.system() == 'Windows')

print ""
if(windws): os.system('cls')
sys.stdout.write("""Player - (X); Computer - (O)\n#-----------#
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
#-----------#\n""")

d = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

x0_k = [1,4,7]
x1_k = [2,5,8]
x2_k = [3,6,9]

x0 = [d[1],d[4],d[7],x0_k]
x1 = [d[2],d[5],d[8],x1_k]
x2 = [d[3],d[6],d[9],x2_k]

y0_k = [1,2,3]
y1_k = [4,5,6]
y2_k = [7,8,9]

y0 = [d[1],d[2],d[3],y0_k]
y1 = [d[4],d[5],d[6],y1_k]
y2 = [d[7],d[8],d[9],y2_k]

d1_k = [1,5,9]
d2_k = [3,5,7]

d1 = [d[1],d[5],d[9],d1_k]
d2 = [d[3],d[5],d[7],d2_k]

mem = [x0,x1,x2,y0,y1,y2,d1,d2]

k = 0

def update():
    global x0, x1, x2, x0_k, x1_k, x1_k
    global y0, y1, y2, y0_k, y1_k, y2_k
    global d1, d2, d1_k, d2_k
    global mem

    x0 = [d[1],d[4],d[7],x0_k]
    x1 = [d[2],d[5],d[8],x1_k]
    x2 = [d[3],d[6],d[9],x2_k]

    y0 = [d[1],d[2],d[3],y0_k]
    y1 = [d[4],d[5],d[6],y1_k]
    y2 = [d[7],d[8],d[9],y2_k]

    d1 = [d[1],d[5],d[9],d1_k]
    d2 = [d[3],d[5],d[7],d2_k]

    mem = [x0,x1,x2,y0,y1,y2,d1,d2]

    for i in mem:
        if i.count('X') == 3:
            sys.exit('Player wins!')

    c = 0
    for i in mem:
        if i.count('X') > 0 and i.count('O') > 0:
            c+=1

    if c == len(mem):
        prnt()
        sys.exit('Tie!')

def prnt():
    if(windws): os.system('cls')
    sys.stdout.write("""Player - (X); Computer - (O)\n#-----------#
| %c | %c | %c |
| %c | %c | %c |
| %c | %c | %c |
#-----------#\n""" % (d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9]) )

def comp():
    global x0, x1, x2, x0_k, x1_k, x1_k
    global y0, y1, y2, y0_k, y1_k, y2_k
    global d1, d2, d1_k, d2_k
    global mem

    for i in mem:
        if i.count('O') == 2 and (' ' in i):
            d[i[3][i.index(' ')]] = 'O'
            update()
            prnt()
            sys.exit("Computer wins!")
            return

    for i in mem:
        if i.count('X') == 2 and (' ' in i):
            d[i[3][i.index(' ')]] = 'O'
            update()
            return

    if d[5] == ' ':
        d[5] = 'O'
        update()
        return

    if d[5] == 'O':
        if d1.count('X') == 2 or d2.count('X') == 2:
            l = []
            if d[2] == ' ':
                l.append(2)
            if d[4] == ' ':
                l.append(4)
            if d[6] == ' ':
                l.append(6)
            if d[8] == ' ':
                l.append(8)

            if len(l) != 0:
                d[l[random.randint(0,len(l)-1)]] = 'O'
                update()
                return

    l = []
    for i in mem:
        if i.count('X') == 1:
            if i[1] == ' ':
                l.append(i[3][1])
    
    if len(l) != 0:
        t = random.randint(0,len(l)-1)
        while d[l[t]] != ' ':
            t = random.randint(0,len(l)-1)
        d[l[t]] = 'O'
        update()
        return
     
    if d[1] == 'X' and d[9] == ' ':
        d[9] = 'O'
        update()
        return
    elif d[9] == 'X' and d[1] == ' ':
        d[1] = 'O'
        update()
        return
    elif d[3] == 'X' and d[7] == ' ':
        d[7] = 'O'
        update()
        return
    elif d[7] == 'X' and d[3] == ' ':
        d[3] = 'O'
        update()
        return

    if d[1] == ' ' or d[3] == ' ' or d[7] == ' ' or d[8] == ' ':
        l = []
        if d[1] == ' ':
            l.append(1)
        if d[3] == ' ':
            l.append(3)
        if d[7] == ' ':
            l.append(7)
        if d[8] == ' ':
            l.append(8)

        if len(l) != 0:
            t = random.randint(0,len(l)-1)
            while d[l[t]] != ' ':
                t = random.randint(0,len(l)-1)
            d[l[t]] = 'O'
            update()
            return

    if x0.count(' ') == 3:
        x0[random.randint(0,len(x0)-1)] = 'O'
        update()
        return
    elif x1.count(' ') == 3:
        x1[random.randint(0,len(x1)-1)] = 'O'
        update()
        return
    elif x2.count(' ') == 3:
        x2[random.randint(0,len(x2)-1)] = 'O'
        update()
        return
    elif y0.count(' ') == 3:
        y0[random.randint(0,len(y0)-1)] = 'O'
        update()
        return
    elif y1.count(' ') == 3:
        y1[random.randint(0,len(y1)-1)] = 'O'
        update()
        return
    elif y2.count(' ') == 3:
        y2[random.randint(0,len(y2)-1)] = 'O'
        update()
        return

while win == 0:
    a = "_"
    while a.isdigit() == False:
        a = raw_input("Block No.: ")
        if a.isdigit() == True:
            if int(a) <= 9 and int(a) >=1:
                if d[int(a)] != ' ':
                    print "Invalid input."
                    a = "_"
            else:
                print "The block no. must lie between 1 and 9."
                a = "_"
        else:
            print "The block no. must be a number between 1 and 9."
        
    a = int(a)
    d[a] = 'X'
    update()

    comp()
    prnt()

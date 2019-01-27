import numpy as np
import random

gamma = 0.8
def bellman(loc,dec):
    global gamma , q , reward_table
    a = (loc[0],loc[1])
    hasil1 = reward_table[a][dec] 
    d0 = q[(loc[0],loc[1])][0]
    d1 = q[(loc[0],loc[1])][1]
    d2 = q[(loc[0],loc[1])][2]
    d3 = q[(loc[0],loc[1])][3]
    hasil2 = max(d0, d1, d2, d3)
    hasil = hasil1 + (gamma * hasil2)
    return hasil


def move(loc,dec):
    if dec == 0 :
        if loc[1] > 0 :
            loc[1] = loc[1] - 1
    elif dec == 1 :
        if loc[1] < 9 :
            loc[1] = loc[1] + 1
    elif dec == 2 :
        if loc[0] < 9 :
            loc[0] = loc[0] + 1
    elif dec == 3 :
        if loc[0] > 0 :
            loc[0] = loc[0] - 1

def r_up(loc):
    global reward
    if loc[1] > 0 :
        y = loc[1] - 1
    else :
        return 0
    return reward[loc[0]][y]

def r_down(loc):
    global reward
    if loc[1] < 9 :
        y = loc[1] + 1
    else :
        return 0
    return reward[loc[0]][y]

def r_right(loc):
    global reward
    if loc[0] < 9 :
        x = loc[0] + 1
    else :
        return 0
    return reward[x][loc[1]]

def r_left(loc):
    global reward
    if loc[0] > 0 :
        x = loc[0] - 1
    else :
        return 0
    return reward[x][loc[1]]

start = [9,0]
x = 10
y = 10
finish = [0,9]
initial = [0,0,0,0]
q_table = {}
walk_record = []
reward = np.loadtxt("DataTugasML3.txt")
states = []
for i in range(x):
    for j in range(y):
        states.append((i,j))

reward_table = {}
for i in range(x*y) :
    reward_table[states[i]] = initial

for dec in range(0,4):
    for i in range(len(reward)):
        for j in range(len(reward[0])):
            loc = [i,j]
            temp = []
            temp.clear
            temp.append(r_up(loc))
            temp.append(r_down(loc))
            temp.append(r_right(loc))
            temp.append(r_left(loc))
            reward_table[(i,j)] = temp

maks = -99999
for i in range(x*y) :
    q_table[states[i]] = initial

for i in range(0,100):
    score = 0
    q = q_table
    end = False
    loc = [9,0]
    while end == False:
        # up = 0 , down = 1 , right = 2 ,left = 3
        dec = random.randint(0,3)
        bell = bellman(loc,dec)
        q[(loc[0],loc[1])][dec] = bell
        if dec == 0 : 
            move(loc,dec)
            score = score + r_up(loc)
        elif dec == 1:
            move(loc,dec)
            score = score + r_down(loc)
        elif dec == 2:
            move(loc,dec)
            score = score + r_right(loc)
        elif dec == 3 :
            move(loc,dec)
            score = score + r_left(loc)

        if loc[0] == finish[0] and loc[1] == finish[1] :
            end = True
    print("score = ",score)
    if maks < score :
        maks = score  
    q_table = q  

print("maks ",maks)    

        








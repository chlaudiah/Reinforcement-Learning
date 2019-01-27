import numpy as np
def move_by_action(action,x,y):
    if action == 0:
        y -= 1
        if y<0:
            return 0
    elif action == 1:
        y += 1
        if y>9:
            return 0
    elif action == 2:
        x -= 1
        if x<0:
            return 0
    elif action == 3:
        x += 1
        if x>9:
            return 0
    return dataTrain[y][x]

#how to make a new environment
def make_an_env(dataTrain,env):
    l=0
    for i in range(len(dataTrain)):
        for j in range(len(dataTrain[0])):
            #print(awal[i][j])
            for k in range(len(env[0])):
                env[l][k] = move_by_action(k,j,i)
                #print(ubah)
            l += 1
    return env

dataTrain = np.loadtxt("DataTugasML3.txt")
env = np.zeros(((len(dataTrain)*len(dataTrain[0]),4)))
print(dataTrain)

#env
env = make_an_env(dataTrain,env)
print(env)
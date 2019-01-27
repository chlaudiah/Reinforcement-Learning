import numpy as np

def QLearning(n):
    goal = False
    state = np.random.randint(initial_state)
    # print(state)
    while state != 9:
        perpindahan = np.where(matriks_reward[state,aksi_range]>=-5)[1]
        aksi = int(np.random.choice(perpindahan,size = 1))
        next_state = aksi

        reward_maks_indeks = np.where(matriks_Q[state,] == np.max(matriks_Q[state,]))[1]
        if reward_maks_indeks.shape[0] > 1:
            reward_maks_indeks = int(np.random.choice(reward_maks_indeks, size=1))
        else:
            reward_maks_indeks = int(reward_maks_indeks)

        nilai_maks_reward = matriks_Q[state,reward_maks_indeks]

        matriks_Q[state,aksi] = matriks_reward[state,aksi] + learning_rate*nilai_maks_reward

        print(np.rint(matriks_Q))
        print('State saat ini: ', state)
        print("Iterasi ke-",n)
        state = next_state

        if (np.max(matriks_Q) > 0):
            score = np.sum(matriks_Q / np.max(matriks_Q) * 100)
        else:
            score = 0

        print("Score: ",score)

matriks_reward = np.matrix(np.loadtxt("DataTugasML3.txt", dtype='i', delimiter='\t'))
matriks_Q = np.matrix(np.zeros(shape=(10,10)))
# print(matriks_reward)

learning_rate = 0.8
initial_state = 10
aksi_range = np.arange(10)
# print(aksi)

QLearning(0)
print()
print(matriks_Q)
jumlah_iterasi = 50
Q_iterasi = []
for i in range(jumlah_iterasi):
    QLearning(i)

trained = (matriks_Q/np.max(matriks_Q)*100)
print("Trained Matriks Q: ",trained)
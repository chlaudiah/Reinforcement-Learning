import environment
import threading
import time
import numpy as np

discount = 0.3
gamma = 0.8 # Initial probability
gamma_decay = 0.99 # Exploration/exploitation tradeoff
actions = environment.actions
states = []
Q = {}
for i in range(environment.x):
    for j in range(environment.y):
        states.append((i, j))

for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
        environment.set_cell_score(state, action, temp[action])
    Q[state] = temp

for (i, j, c, w) in environment.specials:
    for action in actions:
        Q[(i, j)][action] = w
        environment.set_cell_score((i, j), action, w)


def do_action(action):
    s = environment.player
    r = -environment.score
    if action == actions[0]:
        environment.try_move(0, -1)
    elif action == actions[1]:
        environment.try_move(0, 1)
    elif action == actions[2]:
        environment.try_move(-1, 0)
    elif action == actions[3]:
        environment.try_move(1, 0)
    else:
        return
    s2 = environment.player
    r += environment.score
    return s, action, r, s2


def max_Q(s):
    val = None
    act = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val


def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc
    environment.set_cell_score(s, a, Q[s][a])


def run():
    global discount
    global gamma
    time.sleep(1)
    alpha = 1
    t = 1
    # If its taking too long, then restart and try again
    max_run_iter = 5000
    cur_iter = 0
    while True:
        cur_iter += 1
        if cur_iter > max_run_iter:
            cur_iter = 0
            environment.restart_game()

        # Pick the right action
        s = environment.player
        max_act, max_val = max_Q(s)

        # Exploration/Exploitation tradeoff
        if np.random.rand(1) <= gamma:
            max_act = np.random.choice(["up", "down", "left", "right"])
            # print max_act

        (s, a, r, s2) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(s2)
        inc_Q(s, a, alpha, r + discount * max_val)

        # Check if the game has restarted
        t += 1.0
        if environment.has_restarted():
            environment.restart_game()
            gamma *= gamma_decay
            time.sleep(0.01)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

        # Reduce sleep time to get results faster
        time.sleep(0.01)


t = threading.Thread(target=run)
t.daemon = True
t.start()
environment.start_game()
def LSFR(seed='1001', state='0001', cycles=10, size=0):
    if size < 4:
        size = len(state)

    init_state = size * [0]
    for i in range(len(init_state)):
        if state[i] == '0':
            init_state[i] = 0
        elif state[i] == '1':
            init_state[i] = 1
        else:
            return 'Error'

    init_seed = []
    for i in range(len(seed)):
        if seed[i] == '1':
            init_seed.append(i)

    for i in range(cycles):
        print('Cycle nr', i + 1)
        print(init_state)
        FB = 0
        for j in init_seed:
            FB ^= init_state[j]
        init_state = ([FB] + init_state)[0:size]



if __name__ == '__main__':
    LSFR()

def encryption(seed='1110', state='1101', input='0101', size=0):
    output = []
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

    init_input = size * [0]
    for i in range(len(input)):
        if input[i] == '1':
            init_input[i] = 1
        elif input[i] == '0':
            init_input[i] = 0

    for i in range(len(init_state)):
        FB = 0
        output.append(init_state[0] ^ init_input[i])
        for j in init_seed:
            FB ^= init_state[j]

        init_state = ([FB] + init_state)[0:size]

    return output


if __name__ == '__main__':
    print('Wielomian wejściowy:  1101')
    print('Szyfrowanie:   ', encryption(input='0101'))
    print('Deszyfrowanie: ', encryption(input='1100'))

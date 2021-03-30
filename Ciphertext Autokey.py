def encryption(seed='1110', state='1101', text='1001011'):
    output = []

    init_state = len(text) * [0]
    for i in range(len(state)):
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

    init_text = len(text) * [0]
    for i in range(len(text)):
        if text[i] == '0':
            init_text[i] = 0
        elif text[i] == '1':
            init_text[i] = 1
        else:
            return 'Error'

    for i in range(len(text)):
        output.append(init_state[0] ^ init_text[i])
        FB = 0
        for j in init_seed:
            FB ^= init_state[j]
        init_state = ([FB] + init_state)[0:len(text)]
        init_state[0] = init_state [0] ^ init_text[i]

    result = ''.join([str(elem) for elem in output])

    return result


def decryption(seed='1110', state='1101', text='1001011'):
    output = []

    init_state = len(text) * [0]
    for i in range(len(state)):
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

    init_text = len(text) * [0]
    for i in range(len(text)):
        if text[i] == '0':
            init_text[i] = 0
        elif text[i] == '1':
            init_text[i] = 1
        else:
            return 'Error'

    for i in range(len(text)):
        output.append(init_state[0] ^ init_text[i])
        FB = 0
        for j in init_seed:
            FB ^= init_state[j]
        init_state = ([FB] + init_state)[0:len(text)]
        init_state[0] = init_state [0] ^ output[i]

    result = ''.join([str(elem) for elem in output])

    return result


if __name__ == '__main__':
    print('Szyfrowanie:   ', encryption())
    print('Deszyfrowanie: ', decryption(text=encryption()))

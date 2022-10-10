import json

dic = {
    'a': [100, 101, 102], 'b': [103, 104, 105], 'c': [106, 107, 108], 'd': [109, 110, 111], 'e': [112, 113, 114],
    'f': [115, 116, 117], 'g': [118, 119, 120], 'h': [121, 122, 123], 'i': [124, 125, 126], 'j': [127, 128, 129],
    'k': [130, 131, 132], 'l': [133, 134, 135], 'm': [136, 137, 138], 'n': [139, 140, 141], 'o': [142, 143, 144],
    'p': [145, 146, 147], 'q': [148, 149, 150], 'r': [151, 152, 153], 's': [154, 155, 156], 't': [157, 158, 159],
    'u': [160, 161, 162], 'v': [163, 164, 165], 'w': [166, 167, 168], 'x': [169, 170, 171], 'y': [172, 173, 174],
    'z': [175, 176, 177], ' ': [178, 179, 180], ',': [181, 182, 183], '.': [184, 185, 186], '!': [187, 188, 189],
}


def encode(input_message):
    input_message = input_message
    input_message = input_message.lower()
    result = []
    indexes = []
    counter = 0

    # with open('table.json', 'w') as file:
    #     file.write(json.dumps(dic))
    for l_in_message in input_message:
        indexes.append(l_in_message)
        for l_in_dic in dic:
            if l_in_message == l_in_dic:  # проверка равно ли буква из сообщ. на букву из словаря
                if input_message.count(l_in_message) > 1:
                    if counter == 3:
                        counter -= 3
                        result.append(dic[l_in_dic][0] + counter)
                        counter += 1
                    else:

                        result.append(dic[l_in_dic][0] + counter)
                        counter += 1
                elif input_message.count(l_in_message) < 2:
                    result.append(dic[l_in_dic][0])
    print(result)

    with open('Input_text.txt', 'a') as text:
        text.write(' '.join(str(input_message)))

    with open('Ciphertext.txt', 'a') as cipher:
        cipher.write(' '.join(str(result)))

    final = ''

    for o in result:
        final += str(o)

    print('Ciphertext:', final, '\n')


def decode(input_ciphertext):
    input_ciphertext = list(input_ciphertext)
    decoded_text = []
    for a in input_ciphertext:
        for k, n in dic.items():
            for i in n:
                if i == a:
                    decoded_text.append(k)

    print(decoded_text)


if __name__ == '__main__':
    while True:
        print('1.Encode\n'
              '2.Decode\n'
              '3.Help\n'
              '4.Quit\n')

        ask = input('Please, choose function!\n'
                    '-> ')

        if int(ask) == 1:
            message = input('your message->')
            if not message.isdigit():
                encode(message)
            else:
                print('I can encode only latin letters')
        elif int(ask) == 2:
            message = []
            print('enter the ciphertext in the form:\n'
                  "example: [100, 200, 300 ...]")
            num_elements = int(input('Enter number of elements: '))
            for i in range(0, num_elements):
                mess = int(input())
                message.append(mess)
            decode(message)
        elif int(ask) == 4:
            break
        else:
            print('bye!')

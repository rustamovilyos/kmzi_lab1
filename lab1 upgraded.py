from table import dic


def encode(input_message):
    input_message = input_message
    input_message = input_message.lower()
    result = []
    indexes = []
    counter = 0
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

    final = ''

    for o in result:
        final += str(o)
    with open('Ciphertext.txt', 'a', encoding='utf-8') as cipher:
        cipher.write(final)
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


# if __name__ == '__main__':
#     while True:
#         print('1.Encode\n'
#               '2.Decode\n'
#               '4.Quit\n')
#
#         ask = input('Please, choose function!\n'
#                     '-> ')
#
#         if int(ask) == 1:
#             message = input('your message->')
#             if not message.isdigit():
#                 encode(message)
#             else:
#                 print('I can encode only latin letters')
#         elif int(ask) == 2:
#             message = []
#             print('enter the ciphertext in the form:\n'
#                   "example: [100, 200, 300 ...]")
#             num_elements = int(input('Enter number of elements: '))
#             for i in range(0, num_elements):
#                 mess = int(input())
#                 message.append(mess)
#             decode(message)
#         elif int(ask) == 4:
#             break
#         else:
#             print('bye!')

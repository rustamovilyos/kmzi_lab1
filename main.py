from lab1 import encode, decode

if __name__ == '__main__':
    while True:
        print('1.Encode\n'
              '2.Decode\n'
              '3.Quit\n')

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
        elif int(ask) == 3:
            break
        else:
            print('bye!')

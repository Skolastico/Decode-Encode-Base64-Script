import base64


messagearray = ['What do you wanna decode?: ', 'What do you wanna encode?: ']

def start():
    print('What do you want to do? (use the numbers)')
    finalorder = int(input('0 = Decode' + '\n' '1 = Encode' + '\n' + 'Number: '))
    message = input(messagearray[finalorder])
    base64_bytes = message.encode('ascii')
    
    if finalorder == 0:
        message_bytes = base64.b64decode(base64_bytes)
    elif finalorder == 1:
        message_bytes = base64.b64encode(base64_bytes)
    else:
        print("Error Try again")

    print(message_bytes.decode('ascii'))

def restart():
    print('Do you want to do something else ')
    return int(input('1 = Yes' + '\n' '2 = No' + '\n' + 'Number: '))




again = 1
while again == 1:
    start()
    again = int(restart())

input('Press ENTER to exit the script')



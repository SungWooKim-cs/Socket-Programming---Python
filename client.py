##################################
# TITLE: Socket Programming
# AUTHOR: Sung Woo Kim
# ID: 010920689
# Date: 4/11/21
##################################

import socket # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
s.connect((socket.gethostname(), 12344))

while True:
    choice = input('Enter your choice: \n   withdraw, deposit, check_balance, exit:\n')
    s.send(bytes(choice,'utf-8'))   
    
    if (choice == 'deposit'):
        print("Command", choice, "is selected")
        addAmount = input('Input amount: $')  
        if (addAmount > '0' and addAmount.isdigit() == True):
            print(f"Amount of ${addAmount} is entered")
            s.send(bytes(addAmount, 'utf-8'))
            print(s.recv(1024).decode('utf-8'))
        else:
            print('A negative, zero, string, or float number was entered. Please try again.')
            s.send(bytes('0', 'utf-8'))
            print(s.recv(1024).decode('utf-8'))

    elif (choice == 'withdraw'):
        print("Command", choice, "is selected")
        subAmount = input('Input amount: $') 
        if (subAmount > '0' and subAmount.isdigit() == True):
            print(f"Amount of ${subAmount} is entered")
            s.send(bytes(subAmount, 'utf-8'))
            print(s.recv(1024).decode('utf-8'))
        else: 
            print('A negative, zero, string, or float number was entered. Please try again.')
            positive_infnity = 100000000000000000000000000000000000
            positive_infnity = str(positive_infnity)
            s.send(bytes(positive_infnity, 'utf-8'))
            print(s.recv(1024).decode('utf-8'))
            # print(s.recv(1024).decode('utf-8'))
            # s.send(bytes("don't do that", 'utf-8'))

    elif(choice == 'check_balance'):
        print("Command", choice, "is selected")
        updatedBalance = s.recv(1024).decode('utf-8')
        print(f"The balance is ${updatedBalance}\n")
    
    elif(choice == 'exit'):
        print("exiting the program")
        s.close()
        exit()
        
    else:
        print("Please re-enter valid operation name")
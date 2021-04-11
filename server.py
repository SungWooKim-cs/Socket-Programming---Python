##################################
# TITLE: Socket Programming
# AUTHOR: Sung Woo Kim
# ID: 010920689
# Date: 4/11/21
##################################

import socket # Import socket module

currentBal = 100

def deposit(a):
    global currentBal
    if(a > 0):
        currentBal += a
        return currentBal
    else: 
        return -1
    
def withdraw(a):
    global currentBal
    if(currentBal >= a):
        currentBal -= a
        return currentBal    
    else:
        return -1
    
def check():
    return currentBal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
s.bind((socket.gethostname(), 12344)) # Bind to the port
s.listen(5) # Now wait for client connection.
clientSocket, address = s.accept() # Establish connection with client.
print(f'Got connection from {address} has been established!')

while True:
    print(f'The server initialized the bank account')
    print(f'The server is ready to receive requests')
    
    data = clientSocket.recv(1024)
    # print(data)
    
    if(data == b'exit'): 
        clientSocket.close()
        exit()

    elif(data == b'deposit'): #write your code to print account details print(AccBal)
        print(f'Server has received the request')
        print(f'Server is processing the request')
        valueRecved = clientSocket.recv(1024).decode('utf-8') #-1
        # print(valueRecved)
        valueAdded = deposit(int(valueRecved))
        # print(valueAdded)  
        # clientSocket.send(str(valueAdded).encode('utf-8')) #sending an updated value 
        if(valueAdded > 0):
            clientSocket.send(bytes("From Server: Operation succeeded!\n", 'utf-8')) #just to notify that the operation worked
            print(f'Deposit is accepted. New balance is ${valueAdded}\n')
        elif (valueAdded < 0):
            print('Amount cannot be processed\n')
            clientSocket.send(bytes("From Server: Operation failed!\n", 'utf-8')) #just to notify that the operation worked


    elif(data == b'withdraw'): #write your code to print account details print(AccBal)
        print(f'Server has received the request')
        print(f'Server is processing the request')
        valueRecved = clientSocket.recv(1024).decode('utf-8')
        # valueRecved = int(valueRecved)
        # if (valueRecved < 0)
        valueSubed = withdraw(int(valueRecved))
        if(valueSubed >= 0):
            clientSocket.send(bytes("From Server: Operation succeeded!\n", 'utf-8')) #just to notify that the operation worked
            print(f'Withdraw is accepted. New balance is ${valueSubed}\n')
        elif (valueSubed < 0):
            print('Amount cannot be withdrawn\n')
            clientSocket.send(bytes("From Server: Operation failed!\n", 'utf-8')) #just to notify that the operation worked

    elif(data == b'check_balance'): #write your code to print account details print(AccBal)
        Curbal = str(check())
        clientSocket.send(bytes(Curbal, 'utf-8'))
        print(f'Balance is requested. The balance is ${Curbal}\n')

    else:
        print("Waiting for valid operation")

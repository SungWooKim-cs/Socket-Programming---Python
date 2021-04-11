How to run the program: 
	1. run server.py: python3 server.py
	2. run client.py: python3 client.py
	3. Operations: 
		Withdraw: type withdraw
		Deposit: type deposit
		Check Balance: type check_balance
		Exit: type exit

Error checking:
	1. If anything typed other than withdraw, deposit, check_balance, and exit when choosing an operation: prompt "Please re-enter valid operation name".
	2. When negative, float, zero, or string/char amount is entered in Deposit, prompt "A negative, zero, sting, or float number was entered. Please try again" (client). prompt "Amount cannot be withdrawn" and send to client "From Server: Operation failed!"(server).
	3. When trying to withdraw more than what current balance is: receive message from server "From Server: Operation failed!"(client). When negative, float, zero, or string/char amount is entered in Deposit, prompt "A negative, zero, sting, or float number was entered. Please try again" (client). prompt "Amount cannot be withdrawn" and send to client "From Server: Operation failed!"(server).
   
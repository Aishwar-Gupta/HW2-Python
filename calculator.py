def calculator(number1, number2, operator):
	'''
	Conducts the desired operation on numbers.

	This function takes two numbers and an operator to conduct the necessary operation.
	Operators work as follows:
	If the user enters '+': the function performs addition of the two numbers.
	If the user enters '-': the function performs subtraction of the two numbers.
	If the user enters '*': the function performs multiplication of the two numbers.
	If the user enters '/': the function performs division of the two numbers.
	If the user enters '//': the function performs integer division of the two numbers.
	If the user enters '**': the function performs exponentiation of the two numbers.
	Else if the operator does not match: the program exits right away.

	Parameters
	----------
	number1 : float or int
		First number for the operation.
	number2 : float or int
		Second number for the operation.
	operator: String
		Stores the type of operator to be used for calculation.

	Returns
	-------
	float
		Conducts the necessary operation and displays the result.

	Examples
	--------
	>>> Enter the first number: 17.4
	    Enter the second number: 2.6
	    Enter the operation: +
	    20.0

	    Do you wish to exit? n
	    Enter the first number: 20.0
	    Enter the second number: 10
	    Enter the operation: -
	    10.0

	    Do you wish to exit? y

	'''
	if (operator == '+'):
		return (float(float(number1) + float(number2)))
	elif (operator == '-'):
		return (float(float(number1) - float(number2)))
	elif (operator == '*'):
		return (float(float(number1) * float(number2)))
	elif (operator == '/'):
		return (float(float(number1) / float(number2)))
	elif (operator == '//'):
		return (float(float(number1) // float(number2)))
	elif (operator == '**'):
		return (float(float(number1) ** float(number2)))
	else:
		exit()         # Exit the program right away


def input_output():
	'''
	Takes the user input and continues to do operations until user wants to exit.

	This function allows the user to enter runtime inputs for the two numbers and the type of operation.
	It also asks the user if they want to end the process by entering 'y' else it will loop the process.
	It will do the calculation atleast once when the program starts before asking if the user wants to quit.
	It calls the function calculator(number1, number2, operator) and passes the user input for calculations.

	Parameters
	----------
 	none :
		This function takes user inputs and passes to the calculator function
	
	Returns
	-------
	None : default return value
		This function does not return value

	Examples
	--------
	>>> Enter the first number: 8
	    Enter the second number: 2
	    Enter the operation: **
	    64.0

	    Do you wish to exit? n
	    Enter the first number: 4
	    Enter the second number: 3
	    Enter the operation: //
	    1.0

	    Do you wish to exit? y

	'''
	flag = True
	while(flag == True):        # runs the process atleast once and iterates the process
		input1 = input('Enter the first number: ')
		input2 = input('Enter the second number: ')
		operation = input('Enter the operation: ')
		print(calculator(input1, input2, operation))        # Calls the function to perform calculations
		print(' ')
		stop = input('Do you wish to exit? ')
		if (stop == 'y'):        # Checks if the user wants to continue
			flag = False
		elif (stop == 'n'):
			continue



import time

def calculate_time(function):
	'''
	This is a decorator function.

	This function calculates the time taken to execute a function.
	It stores the start and end time and prints the time taken by the passed function to execute.

	Parameters
	----------
	function_time() : function as a parameter
		The function whose execution time is to be calculated.

	Returns
	-------
	Null
		default return from the function

	Examples
	--------
	>>>Total time 2.00000006982315

	'''
	def wrapper():
		'''
		This function adds the functionalities to the passed function

		It calculates the time taken to execute a function by recording the start and end times.

		Parameters
		----------
		None : no parameters
			Since it is inside a function it gets executed every time the parent function is called.

		Returns
		-------
		function : wrapper
			It returns the wrapper function

		Examples
		--------
		>>> Total time 2.00000065103409

		'''
		start = time.time()
		function()
		end = time.time()
		total_time = end - start
		print (f'Total time {total_time}')
	return wrapper


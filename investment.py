def calculate_apr(principal, interest_rate, years):
	'''Calculates money made on an investment.
	
	The calculate_apr function will calculate the amount of money accumulated over a period of time.
	It uses the interest_rate (in decimal format) and the time in years to calculate the increased principal.

	Parameters
	----------
	principal : int greater than 0
		The amount of money invested.
	interest_rate: float greater than 0
		The interest rate received per year on the investment
	years : int greater than 0
		The number of years money was invested

	Returns
	-------
	float
		The amount that will accumulate over the period of time at a given rate of interest

	Examples
	--------
	>>> calculate_apr(500, 0.03, 65)
	3414.9913672928196
	>>> calculate_apr(1000, 6, 40)
	False
	>>> calculate_apr(-1000, -0.03, -30)
	False
	>>> calculate_apr(1000, 0.1, 50)
	117390.85287969573
	'''

	if (principal > 0 and isinstance(interest_rate, float) and interest_rate > 0 and years > 0):     #validate the input variables
		while(years > 0):      # iterate calculations for the number of years
			principal = float( principal * (1 + interest_rate))
			years -= int(1)
		return principal
	else:
		print('False')


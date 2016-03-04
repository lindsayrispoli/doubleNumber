number = input("What number should I double? ")

#while error == True:
	#number = input("Try again: ")
	
try: # try to do this line, does not definitely do it
	number = float(number) 
	#Could put the doubling line here
	# But! try block is only for exception causers 
	
except ValueError: # for the exception  
		#error = True
	print("Sorry, that's not a number.")

else:
	print("Double that is {}.".format(number * 2))
number = input("What number should I double? ")

converted = False 

while not converted: #when converted = true or not false, keep running loop 
	try: # try to do this line, does not definitely do it
		number = float(number) 
	
	except ValueError: # for the exception  
		number = input("Sorry, that's not a number. Try again. ")

	else:
		converted = True
		
		print("Double that is {}.".format(number * 2))
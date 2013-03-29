def reverse(number):
	result=0
	while number > 0:
		result=(result*2)+number%2
		number=number/2
	return result
print reverse(int(raw_input()))

		

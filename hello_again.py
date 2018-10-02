#include the Numpy libary 
import numpy as np #tells computer what to use

#define the main function
def main():
	i = 0	#declare integer i, set to 0
	x=119.0 	#declare a float x, with val 119
	
	
	for i in range(120):	#loops i from 0 through 119
		if ((i%2)==0):	#if i is even 
			x+=3 	#adds 3 to x
		else:		#if i odd
			x-=5	#x = x-5
			
	s = "%3.2e" % x	#make a string that sows
					#x with scientific notation
					
	print (s)

#now the rest of the program 
if __name__ == "__main__":	#this is us naming the function
	main()
	
#continue
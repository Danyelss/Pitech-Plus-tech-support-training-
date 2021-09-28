import datetime
import sys

def get_details():
	print ("Python", end =" ")
	i = 0
	while sys.version[i] != ' ':
		print (sys.version[i], end ="")
		i += 1


	now = datetime.datetime.now()
	print ("\nCurrent date and time: " + now.strftime("%d-%m-%Y %H:%M:%S"))

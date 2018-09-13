#! /usr/local/bin/python3

class myexc(Exception): ## {

	def __init__(self,msg): ## {
		print (msg);
	## }



## }

a = 3;
b = 4;

try:
	if (a < b):
		raise myexc("myexc occurred");
except myexc:
	print (" [FTE] error occurred.");

import sys

numberGiven = int(sys.argv[1])
remainder = (numberGiven % 2)
if ((remainder) == 0) :
   print ("even")
else:
   print ("odd")   
import sys
tries = 0
numerator = int(sys.argv[1])
denominator = int(sys.argv[2])
percentage = 100/(denominator/numerator)
desiredPercentageInverted = int(sys.argv[3])
desiredPercentageNotInverted = (100 - desiredPercentageInverted)
print (f'percentage = {percentage}')
print ( )
percentageTries = 100
while percentageTries > desiredPercentageNotInverted:
    print (100-(percentageTries*((100-percentage)/100)))
    percentageTries = percentageTries*((100-percentage)/100)
    tries = tries + 1
print ( )
print (f'You would have to play this lottery {tries} times to have a good chance of winning.')

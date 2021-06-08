tries = 0
numerator = 1
denominator = 10
percentage = 100/(denominator/numerator)
print (f'percentage = {percentage}')
print ( )
percentageTries = 100
while percentageTries > 50:
    print (100-(percentageTries*((100-percentage)/100)))
    percentageTries = percentageTries*((100-percentage)/100)
    tries = tries + 1
print ( )
print (f' You would have to play this lottery {tries} times to have a good chance of winning.')

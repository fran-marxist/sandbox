import sys

averageTestScore = ((firstTestResult + secondTestResult + thirdTestResult + fourthTestResult)/4)
testScoreSum = ((firstTestResult + secondTestResult + thirdTestResult + fourthTestResult))
if (averageTestScore> 7 and averageTestScore< 10) or (averageTestScore== 7):
    print (f"You passed with an average score of {averageTestScore}!")
elif ((averageTestScore> 5 and averageTestScore< 10) or (averageTestScore == 5)):
    print (f"You can still do the tests again, but you passed. Your average score was {averageTestScore}.")
elif (averageTestScore< 5):
    print (f"You didn't pass, do the tests again. Your average test score was {averageTestScore}. You need {28 - (testScoreSum)} more total points to pass.")
elif (averageTestScore == 10):
    print (f"You got a perfect score of {averageTestScore}! You are a truly stellar student!")  
if (averageTestScore> 10):
    print ("Error: Your average test score is more than 10. Please submit your results again.")
    ")
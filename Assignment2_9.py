print("Write a program which accept number from user and return number of digits in that number")

def  Count_Digit(num):
	iCnt=1
	while iCnt<=num:
	
		num=num/10
		iCnt=iCnt+1

	return iCnt 

num=int(input("Enter the Numer->"))
Ret=Count_Digit(num)
print("Number of Digits are->",+Ret)
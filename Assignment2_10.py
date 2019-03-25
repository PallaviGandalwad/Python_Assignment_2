print("Write a program which accept number from user and return addition of digits in that number")
print("\n")

def Addition_Digit(num):
	idigit=0
	while num>0:
		idigit+=num%10
		num=num//10
	return idigit

num=(int(input("Enter number->")))
Ret=Addition_Digit(num)
print("Addition of Digit is->",+Ret)
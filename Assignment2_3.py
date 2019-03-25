#Write a program which accept one number from user and return its factorial.


def Factorial(num):
          iAns=1
          while num>0:
                    iAns=iAns*num
                    num=num-1
          return iAns

x=int(input("Enter number->"))
print("Factorial of number",x,"is->",Factorial(x))
         

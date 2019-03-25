#Write a program which accept one number and display below pattern.
#Input :5
print("Pattern Output :")
#                  * * * * *
#                  * * * *
#                  * * *
#                  * *
#                  *

def Pattern(n):
          for i in range(n):
                    j=i+1
                    while j<=n:
                              print("*",end=" ")
                              j+=1
                    print("\n")

x=(int(input("Enter thenumber->")))
Pattern(x) 

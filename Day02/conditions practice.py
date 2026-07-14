            #--------Question 1-----------
 # ---------WAP to check whetherinput no is even or odd?--------- 

num=int(input("Enter number :"))

if(num%2==0):
    print(num,"is even number")
else:
    print(num,"is odd number")    


            #----------Question 2------------
  # -------WAP to check greatest of 3 no entered by user -----------

a=int(input("Enter your number 1 :"))
b=int(input("Enter your number 2 :"))
c=int(input("Enter your number 3 :"))

if(a>=b and a>=c):
    print(a,"is the greatest of all.")
elif(b>=c ):
    print(b,"is the greatest of all.")
else:
    print(c,"is the greatest of all.")



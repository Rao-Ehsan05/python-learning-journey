    #Python basics
    #  print ("Python basics start from here") # symbol is used for comment it is not printed

name="RAO EHSAN"
age=20
print("My name is :",name)
print("My age is :",age)
            # We can also check type of our variable

print(type(name))
print(type(age))

 
    # now lets perform arithmetic operations

a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)      #for division
print(a%b)      #for finding remainder
print(a**b)     #for power a^b


    #now lets perform relational operators

a=15
b=12
print(a == b)
print(a > b)
print(a < b)
print(a != b)


    # now lets perform assignment operations


a=12
a +=10          #we can also write it as a =a+10
print(a)

b=14
b -=10
print(b)


    #now lets check logical operations


print(not True)
a = 15
b = 10
print(not(a<b))

a=True
b=False
print("And operation:",a and b)

a=True
b=False
print("Or operation:",a or b)

# there are 2 types------> type conversion & type casting.....type conversion is automatic and other is manual
#type----->1


a=2
b=2.24          #here a is int type and b is float type so int type is automatically converted to float

print(a+b)

#type-------->2

a=int("2")      #as a="2" so it was string but now we manually converted it to int by writing a=int("2")
b=1.5

print(a+b)


# Now lets take input by user 

#input("Enter your name : ")----->we can take value from user in this way

name=input("Enter your name :")
print  ("welcome", name)

#input by user type is always string so we have to convert it manually whatever type we want

a=int(input("enter value:"))
print(type(a),a)
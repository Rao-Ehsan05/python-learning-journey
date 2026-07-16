age1 = 18
age2 = 38
age3 = 28
age4 = 11
age5 = 20
age6 = 19
print("ages of students are :", age1,age2,age3,age4,age5,age6)


#       --------For the same work we can store ages in a list-----------

age = [18, 38, 28, 11, 20, 19]
print("ages of students are :",age)
print(type(age))

                # --------------   Difference  properties of string and lists -------------


student=["Ali",18,"Multan"]     # In python listing we can store data of different types(int,string ,float    etc.)
print(student)

#  ---------   In python strings are immutable while lists are mutable   -------means we can access as well as can change data in a list....
print(student[2])
student[2]="Karachi"            # --- here we changed value at index 2
print(student)

str=("he is from multan")
print(str[6])               #   here my output was f bcz at index 6 there is f
 #    -----    str[6]="z" -------   if we try to assign value in string there came an error but in list we can assign value


 # ------------ we can also perform slicing in listting ----------------

city=["Multan", "Karachi", "Lahore", "Peshawar"]
print(city[1 : ])   #   As we don't write ending index so till end it is printed
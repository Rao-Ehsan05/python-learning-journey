# str1='i am rao ehsan'       #we can also write in single quotes
# print(str1)

# str2="I'm rao Ehsan"        #if we've to use single quote inside string quotes we use double quotes
# print(str2)

#now we use escape sequence characters such as tab and next line etc

str1="I'm Rao Ehsan.\nI'm a student"

print(str1)

str1="I'm Rao Ehsan.\tI'm a student"
print(str1)

            # --------------Concatenation--------> adding 2 strings

str1="this is my "
str2="python lecture 2."
print(str1 + str2)

            # -----------for finding length of string-----------


str1="Hello world !"        # As i'm using 2spaces so it will also be included in its length 
print(len(str1))


            # --------------Indexing-------->we can check which no is present at which position


a="My teammates"
print(a[3])                      # print(a[3])----> we can check it like this.....we use square brackets...
                                # indexing starts from 0 digit and space is also given index no....
print(a[2])


            # ------------- Slicing in string-----------

print(a[0 : 3])         #starting index is written but ending not.....and all among them is also included
print(a[3 : 12]) 
print(a[0 : len(a)])    # in slicing ending index we can also write as its length instead of writing no
print(a[0 : ])          #if we don't write end index it is also codsiderd till end
print(a[-6:-2])        #we can also give them negative marking which starts from right to left..



            #         functions in string--------> 

            #------------ ends with function-----------------


string="I'm learning python"
print(string.endswith("learning"))     #As it ends with python so it's output is false.


                # -------------capitalize function----------------


str="how are you? "
print(str.capitalize())  
print(str)              # here for 1st print our sentence 1st letter is capitalized but for next print it doesn't
                #  To make changes in actual string we write it as given below

str=str.capitalize()
print(str)                



                # -------------Replace function--------------


repl="I'm learning python from code with harry."
print(repl)
print(repl.replace("code with harry","Ragav gark"))
print(repl.replace("i","a"))        # we can also replace  a single digit from code

                # --------------Find function-------------

str="i'm a student of university"
print(str.find("student"))          #it tells us that at which index our data is present


                #--------------Count function----------------

str="Rao Ali and Rao Hassan is my best friend"
print(str.count("Rao"))
print(str.count("a"))               # we can also count how many times a single character exist



     
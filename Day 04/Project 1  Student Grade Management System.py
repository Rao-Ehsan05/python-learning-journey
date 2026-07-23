# >>>>>>>>>>>>>>>>>>   Project 1: Student Grade Management System   >>>>>>>>>>>>>>>>>>>>>>>>>>>

# Create a Python program that:

#        1.   Takes the names of 5 students from the user.
#        2.   Takes the marks of each student.
#        3.   Stores the names and marks in separate lists.
#        4.   Displays all students with their marks.
#        5.   Finds and displays the student who scored the highest marks.



#       >>>>>>>>>>>>>>>>>>>>>>>>   Solution   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#       >>>>>>>>>>>>>>>>>>>>>>>>   part1      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print("==============  Enter Student's names =================")

students=[]

students.append(input("\n Enter name of 1st student :"))
students.append(input("\n Enter name of 2nd student :"))
students.append(input("\n Enter name of 3rd student :"))
students.append(input("\n Enter name of 4th student :"))
students.append(input("\n Enter name of 5th student :"))

#       >>>>>>>>>>>>>>>>>>>>>>>>>  part2       >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print("\n ==============  Enter Student's marks =================")

marks =[]

marks.append(int(input("\n Enter marks of 1st student :")))
marks.append(int(input("\n Enter marks of 2nd student :")))
marks.append(int(input("\n Enter marks of 3rd student :")))
marks.append(int(input("\n Enter marks of 4th student :")))
marks.append(int(input("\n Enter marks of 5th student :")))

#       >>>>>>>>>>>>>>>>>>>>>>>>>   part3      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("\n ============== Student's names =================")
print(students)

print("\n============== Student's marks =================")
print(marks)

print("\n ============== Student's Record =================")

print(students[0],"=",marks[0])
print(students[1],"=",marks[1])
print(students[2],"=",marks[2])
print(students[3],"=",marks[3])
print(students[4],"=",marks[4])

highest_marks = marks[0]
topper_name = students[0]

if ( marks[1] > marks[0] ) :

   highest_marks = marks[1]
   topper_name = students[1]

if ( marks[2] > marks[1] ) :
  
   highest_marks = marks[2]
   topper_name = students[2]

if ( marks[3] > marks[2] ) :

   highest_marks = marks[3]
   topper_name = students[3]

if ( marks[4] > marks[3] ) :

   highest_marks = marks[4]
   topper_name = students[4]

print("\n ============== Topper  =================")

print(topper_name ,"=",highest_marks )

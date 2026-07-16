#      >>>>>>>>>>>>>> WAP in which we take 3 favorite movies names from user and store them in a list >>>>>>>>>>>>>>>>>>>>

movies = []

mov1 = input("Enter mov 1 :")
mov2 = input("Enter mov 2 :")
mov3 = input("Enter mov 3 :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)



# >>>>>>>>>>>> Another method for same program  >>>>>>>>>>>>>>>>>>

movies = []
movies.append(input("Enter your 1st movie :"))
movies.append(input("Enter your 2nd movie :"))
movies.append(input("Enter your 3rd movie :"))
print(movies)



#  >>>>>>>>>>>>>>>>>  WAP to count A grades in a tuple >>>>>>>>>>>>>>>>>

grade = ("A","B","A","C","A","D","A","D","C")
print("Grade A is of ",grade.count("A"),"students")


#  >>>>>>>>>>>>>>>>  WAP to store above grades in a list and sort them from A -> B   >>>>>>>>>>>>>>>>>>>>

grade = ("A","B","A","C","A","D","A","D","C")
print(grade)                # it prints tuples  

grade_list = list(grade)
print(grade_list)           # it prints list

grade_list.sort()
print(grade_list)           # here it is sorted

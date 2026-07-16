# ---------------------- Here we will discuss some methods in lists or  simply its specific functions ------------------------


# ------------ append function means adding value at end of list --------------- 



list= ["apple", "orange", "banana"]
print(list)
list.append("mango")
print(list)


 # ------------------  sorting method   -------------------

 # >>>>>>   For ascending order >>>>>>>>>>>>



list= [8,5,3,0,98,1]
print(list)
list.sort()
print(list)

 #  >>>>>>> it can also be performed on characters

list= ["apple", "orange", "banana"]
list.sort()
print(list)



 # >>>>>    For descending order  >>>>>>>>>>>

list= [8,5,3,0,98,1]
print(list)
list.sort(reverse=True)
print(list)


 # ----------- Reverse method ----------------

list= ["apple", "orange", "mango", "banana"]
list.reverse()              # here list is reversed 1st digit goes at last last comes 1st ,2nd at 3rd and 3rd at 2nd
print(list)


 # -----------  Insert method ------------


list= [8,5,3,0,98,1]
list.insert(4,1000)         # in insert function inside() 1st we write index at which index we want change and then  write value which we want 
print(list)


 # ------------ Remove method and pop method ----------  >>>>remove method removes 1st occurence of element and pop removes element from index


list=[12,45,78,34,12,75,78]
list.remove(12)                     # here it removes value 12 which is present 1stly
print(list)

list=[12,45,78,34,12,75,78]
list.pop(3)                         # here it removes value present at index 3.....
print(list)


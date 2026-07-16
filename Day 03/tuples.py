#   -------   Like string tuples are also immutable   --------------

tup= (12,45,32,14)              # syntax same as list but use we use() instead of[]
print(tup)
print(type(tup))
print(tup[2])
                    # tup[2]=15   >>>>>>>>>>>>>>>>>>>>>>>   we can't perform assignment operation in tuple
                    # print(tup)        >>>>>>>>


tup = (1,)     
print(type(tup))            #   we have to use comma after digit in case of tupple
tup = (1)
print(type(tup))            #    in this case as there is no comma so its type is int

#   >>>>>>>>>>>>>>>  we can also perform slicing in tuple like string/list   >>>>>>>>>>>>>>>>>>>>>>

tup = (12,34,43,67,4,56,34,67,)
print(tup[2 : 6])


# >>>>>>>>>>>>>>>>>>>   Method of tuple   >>>>>>>>>>>>>>>>>>>>>


tup = (12,34,43,67,4,56,34,67,)
print(tup.index(67))                #   in tuple index method we find index at which our element is present
print(tup.count(34))     
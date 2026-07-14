age=int(input("Enter your age :"))

if(age>=18):
    print ("can vote")
else:
    print("Can't vote")
    #----------For lights----------
    
light="green"  

if(light=="red"):
    print("As light is red you should Stop")
elif(light=="green"):
    print("As light is green you should Go")
elif(light=="yellow"):      # as our condition is proven true so code ends above and this condition is not checked
    print("As light is yellow you should Look")

# if condition can be printed several times if it is true but elif once proven true code stop checking  other conditions 

light="blue"  

if(light=="red"):
    print("Stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):      
    print("Look")   
else:
    print("Light is broken")       # we can see there is a tab/4 spaces in our every print line after condition this is known as indendation and it is very important

#functions = block of statements that perform a specific task
# reduces redundency
def calc_sum(a,b): #function defination
    sum=a+b
    print(sum)
calc_sum(9,10) #function call

#built-in functions
print()
len()
type()
range()
#user-defined functions=defined by user 

#default parameter
def calc_sum(a=1,b=1): #assign random values to parameter
    sum=a+b
    print(sum)
calc_sum() #even if we dont pass arguments ,code will run default parameter

def calc_sum(a,b=1): #if only one parameter has to assign no, in that case 2nd parameter has to ass value not the first one
    sum=a+b
    print(sum)
calc_sum()

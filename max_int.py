#user can take any number he choses
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
#user can only use postive number
max_int=0
#works only if user puts in poritive number, if negative is put in dose not work.
while num_int >=0:
    #the next and the next and next
    num_int = int(input("Input a number: "))
    if max_int < num_int:
        max_int=num_int
print("The maximum is", max_int)    # Do not change this line


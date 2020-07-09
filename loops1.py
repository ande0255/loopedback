#Comments that begin with # are overlooked by Python!

print ('Hello world!')     #Generic Hello World!

print ('What is your name?')    #Name Question
myName = input()   #Person inputs their name
print ('It is good to meet you, ', + myName)     #Pleasantries!
print ('The length of your name is:')    #Name Length
print (len(myName))     #Prints name length in Interger value
print ('What is your age?')   #Age Question
myAge = input()     #Person inputs their age
print ('You will be ' + str(int(myAge) + 1) + ' in a year!') #Age + 1

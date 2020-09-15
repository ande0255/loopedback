 
#Getting deeper into it!

number = "7,230;403 826.271:112,165"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val)for val in values])

#Kapow! I have no idea what I just coded but lets see what happens!
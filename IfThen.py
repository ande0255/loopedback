name = input('Please tell me your name: ')
rawAge = input('Please tell me your age: ')
age = int(rawAge)

if age >= 21:
    print(name, 'you are 20 or older and can come in!')
elif age >= 18: 
    print('You are not allowed to drink, but you may come in.')
else:
    print('You are too young, go home and learn Python!')
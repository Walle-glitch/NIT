def greet(user_name):
    print(f'hello {user_name}. how are you today?')
    
user_name = input('what is your name? ')

greet(user_name)
print('that is all for today.')


def avg(a, b):
    return (a  +  b) / 2
x = int(input('First number: ')) 
y = int(input('Second number: '))
res = avg(x, y)
print(f'The average value is {res}')

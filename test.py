print('range')
for x in range(10):
    print(x)

print('function example1')
def f(x,y):
    return x+y

print(f(1,2))

print('function example2')
def p3(x):
    print(x)
    print(x)
    #return none
    print(x)
print(p3('Hello'))
print('function example3')
x=p3('Hello')
type(x) #None type

print('while')
x=int(input())
while x>0:
    print(x)
x=1
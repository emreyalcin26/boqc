Task 1.
from random import randrange

u = []
v = []
n=7

for i in range(n):
    u.append(randrange(-10,11))
    v.append(randrange(-10,11))
    
print("the elements of u are",u)
print("the elements of v are",v)

Task2.
print("the elements of u are",u)
print("the elements of v are",v)
# 3 * u
for i in range(len(u)):
    u[i] = 3 * u[i]
print("3u is",u)

# 2 * v
for i in range(len(v)):
    v[i] = 2 * v[i]
print("2v is",v)

# 3u - 2v
result=[]
for i in range(len(v)):
    result.append(3*u[i]-2*v[i])
print("the elements of (3u - 2v) are",result)

Task3.
u_2=[]
for i in range(len(u)):
    u_2.append(4*u[i])
    print(u[i],": 4u ->",u_2[i]) #4u

length_square=0
length_square_2=0

for i in range(len(u)):
    length_square = length_square + u[i]**2 #значение под корнем
    length_square_2 = length_square_2 + u_2[i]**2 #значение под корнем
    
u_length= length_square**0.5
u_length2= length_square_2**0.5


print("length of u are",u_length)
print("4 * length of u is",4 * u_length)
print("length of 4u are",u_length2)

Task4.
from random import randrange

u = [1,-2,-4,2]
print("elements of u are ",u)

r = randrange(9)
r = r+1
r = r/10
print("elements of random numbers are ",r)

new_vector=[]
for i in range(len(u)):
    new_vector.append(-1*r*u[i])
print("elements of new_vector are ",new_vector)    

length_square=0
for i in range(len(new_vector)):
    length_square = length_square + new_vector[i]**2 #значение под корнем
    
new_length= length_square**0.5
print("length of new_length are",new_length)
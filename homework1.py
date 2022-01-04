 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 1
#
 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 #2 

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 3

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 4

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 5

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 6

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 7

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 #8
n1=float(input('please enter the first number '))
n2=float(input('please enter the second number '))

if n1>n2 :
    print(f'{n1} is bigger than {n2} ')
    print(n1,'is bigger than',n2)# same format as in line 6
    print('{} is bigger than {}'.format(n1,n2))# same format as in line 6
else:
    print('{} is the bigger '.format(n2))

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 # 9
numb1= float(input('please enter a namber'))
numb2= float(input('please enter a namber'))
numb3= float(input('please enter a namber'))

if numb1 >= numb2 and numb1 >=numb3:
    print(numb1)
elif numb2>numb1 and numb2>=numb3:
    print(numb2)
else:
    print(numb3)

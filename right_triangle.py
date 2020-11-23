print('Author : Sherwin Cunanan')
print('Subject: INS101M\n')

print('**** This program prints a right triangle.                  ****')
print('**** It requests for the length of the width of a triangle. ****')
print('**** Then it creates a right triangle based from the dimesion provided. ****')

print('Disclaimer: \n\tThis program does not provide input validation,\
so please enter correctly the requested action.\n')

dimension = int(input('Please enter the dimension of the triangle : '))      

print('\nNormal Right Triangle leaning to the right')

for y in range(dimension,0,-1):
    space_count = y
    for x1 in range(0,space_count - 1):
        print(' ',end='')
        
    for x in range(0,dimension - space_count):
        print('*',end='')      
        space_count += 1
    print('*')

print('\nInverted Right Triangle leaning to the right')

for y in range(0,dimension):
    space_count = y
    for x1 in range(0,space_count):
        print(' ',end='')
        
    for x in range(1,dimension - space_count):
        print('*',end='')      
        space_count += 1
    print('*')

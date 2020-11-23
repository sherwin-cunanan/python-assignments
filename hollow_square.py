print('Author : Sherwin Cunanan')
print('Subject: INS101M\n')

print('**** This program prints a hollow square.  ****')
print('**** This program requests for the length of the side of a square. ****')
print('**** Then it creates a hollow based from the dimesion provided. ****\n')

print('Disclaimer: \n\tThis program does not provide input validation,\
so please enter correctly the requested action.\n')

squareLength = int(input('Please enter the size of a square : '))
print('\n')

if squareLength > 2:
    for y in range(0,squareLength):
        ### 1st column
        print('*',end='')

        ### 1st and last row
        if (y == 0) or (y == squareLength - 1):
            for x in range(0,squareLength - 2):
                print('*',end='')
            
        ### Middle row
        else:
            for x in range(0, squareLength -2):
                print(' ',end='')

        ### Last column
        print('*')
else:
    print('Can not print a hollow square')        
    

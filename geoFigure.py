#!/bin/env python3

def displayAuthor():
    print('Author : Sherwin Cunanan')
    print('Subject: INS101M\n')

def displayHollowSquareDesc():
    print('\n**** This program prints a hollow square.')

def displayRightTriangleDesc():
    print('\n**** This program prints a normal and an inverted right triangle leaning to the right.')
    
def displayDisclaimer():
    print('Disclaimer: \n\tThis program does not provide input validation,\
so please enter correctly the requested input.\n')

class GeoFigure:
    def __init__(self,size):
        self.size = size

    def createHollowSquare(self):
        dimension = self.size

        displayHollowSquareDesc()
        
        if dimension < 3:
            return(print('Cannot print a Hollow Square'))

        print('\nHollow Square')
        for y in range(0,dimension):
        ### 1st column
            print('*',end='')

        ### 1st and last row
            if (y == 0) or (y == dimension - 1):
                for x in range(0,dimension - 2):
                    print('*',end='')
            
        ### Middle row
            else:
                for x in range(0, dimension -2):
                    print(' ',end='')

        ### Last column
            if (dimension > 2):
                print('*')

    def createRightTriangle(self):
        dimension = self.size
        
        displayRightTriangleDesc()

        if dimension < 2:
            return(print('Cannot print a triangle'))
        
        print('\nNormal Right Triangle leaning to the right')

        for y in range(dimension,0,-1):
            space_count = y
            for x1 in range(0,space_count - 1):
                print(' ',end='')
            for x in range(0,dimension - space_count):
                print('*',end='')      
                space_count += 1
            print('*')

    def createInvertedTriangle(self):
        dimension = self.size
        
        if dimension < 2:
            return(print('Cannot print an inverted triangle'))

        print('\nInverted Right Triangle leaning to the right')
        for y in range(0,dimension):
            space_count = y
            for x1 in range(0,space_count):
                print(' ',end='')
            for x in range(1,dimension - space_count):
                print('*',end='')      
                space_count += 1
            print('*')

if __name__ == '__main__':
    displayAuthor()
    displayDisclaimer()
    x = int(input('Please enter the dimension of the figure: '))
    GeoFigure(x).createRightTriangle()
    GeoFigure(x).createInvertedTriangle()
    GeoFigure(x).createHollowSquare()
    
    

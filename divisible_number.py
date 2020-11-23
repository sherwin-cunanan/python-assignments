#!/bin/env python3

DIVISIBLE_LIST = [2,3,5,6]

def displayDescription():
    print('Author : Sherwin Cunanan')
    print('Subject: INS101M\n')
    print('**** This program checks if the number series is divisible.       ****')
    print('**** It requests for lower limit and upper limit.                 ****')
    print('**** Then it checks if it is divisible given the list of numbers. ****')

def displayDisclaimer():
    print('Disclaimer: \n\tThis program does not provide input validation,\
so please enter correctly the requested input.\n')


def getDivisibleList(x):
    divisibleByList = x
    print('**** ',list(divisibleByList),'  ****\n')
    displayDisclaimer()  
    return divisibleByList

def getInputLimits():
    lowerlimit = int(input('Please enter the lower limit number : '))
    upperlimit = int(input('Please enter the upper limit number : '))
    print('')
    return lowerlimit, upperlimit

def processDivisible():
    ### get Divisible List
    divisibleByList = getDivisibleList(DIVISIBLE_LIST)

    ### get upper and lower limits
    lowerlimit, upperlimit = getInputLimits()

    divisibleBy = []
        
    for number in range(lowerlimit,upperlimit + 1):
        ### Initialize counters, indicators
        divisibleBy.clear()
        countDivisibleBy = 0
        isDivisible = False

        for x in range (0, len(divisibleByList)):  
        ### checks if the number series is divisible based from the divisible list
            if number % divisibleByList[x] == 0:
                divisibleBy.append(True)
                isDivisible = True
                countDivisibleBy += 1
            else:
                divisibleBy.append(False)
    
        ### prints 'is divisible' if the number is divisible
        if isDivisible:
            print(number,'is divisible by ',end='')
        else:
            print(number,end='')

        ### display separators, comma or and
        z = 0
        for x in range (0, len(divisibleBy)):
        
            if divisibleBy[x] == True:
                print(divisibleByList[x],end=' ')
                z += 1
            ### checks if a comma or and should be place 
                if countDivisibleBy > 1:
                    if (countDivisibleBy - 1) == z:
                        print('and ',end='')
                    if (countDivisibleBy - 1) > z:
                        print(', ',end='')
        print('')
        
        
def main():
    displayDescription()
    processDivisible()
     
if __name__ == '__main__':
    main()


        
        
    
        
    
            

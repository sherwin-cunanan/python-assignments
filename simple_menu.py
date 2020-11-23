import assignment5

assignment5.displayDescription()

ticketList = [['Ticket No.','Description','Status'],
              [1,'Ticket No. 1','Open'],
              [2,'Ticket No. 2','Closed'],
              [3,'Ticket No. 3','Open'],
              [4,'Ticket No. 4','Open'],
              ]

header1 = ticketList[0][0]
header2 = ticketList[0][1]
header3 = ticketList[0][2]

def doOption1(z):
    print('Here are your Open tickets\n')
            
    for x in range (1, z):
        if ticketList[x][2] == 'Open':
           print(header1,': ',ticketList[x][0])
           print(header2,': ',ticketList[x][1])
           print(header3,': ',ticketList[x][2],'\n')

def doOption2(z):
    print('Here are All your tickets\n')
    #print(ticketList)
    for x in range (1, z):
        print(header1,': ',ticketList[x][0])
        print(header2,': ',ticketList[x][1])
        print(header3,': ',ticketList[x][2],'\n')

def doOption3(z):
    ticketItem = []
    ticketItem.append(z)
    itemDesc = input('Enter ticket description : ')
    ticketItem.append(itemDesc)
    ticketItem.append('Open')
    ticketList.append(ticketItem)

def doOption4():
    ticketNum = int(input('Enter ticket number to update : '))
    print(header1,': ',ticketList[ticketNum][0])
    print(header2,': ',ticketList[ticketNum][1])
    ticketList[ticketNum][1] = input('New Description : ')
    print(header3,': ',ticketList[ticketNum][2])
    ticketList[ticketNum][2] = input('New Status : ')


def main():
    isQuit = False
    while not isQuit:
   
        assignment5.displayMenu()
        getInput = int(input('Enter action ? '))
        z = len(ticketList)

        if getInput == 0:
            print('Thank you, have a nice day')
            isQuit = True

        if getInput == 1:
            doOption1(z)          
                  
        if getInput == 2:
            doOption2(z)       

        if getInput == 3:
            doOption3(z)

        if getInput == 4:
            doOption4()                
        
if __name__ == '__main__':
    main()

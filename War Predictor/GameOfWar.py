import time

playerOne = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
             11,11,11,11,12,12,12,12,13,13,13,13]
playerTwo = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
             11,11,11,11,12,12,12,12,13,13,13,13]


tableCards = []

def endGame(stackOne, stackTwo):
    if len(stackOne) == 0 or len(stackTwo) == 0:
        print("game over")
        quit()

def whoWins(stackOne, stackTwo):
    endGame(stackOne, stackTwo)
    
    cardOne = stackOne[-1]
    cardTwo = stackTwo[-1]
    
    print(cardOne, cardTwo)
    print("player one", stackOne, "player two", stackTwo, "cards on table", tableCards)
    print("")

    
    if cardOne > cardTwo:
        tableCards.append(cardOne)
        tableCards.append(cardTwo)
        stackOne.pop()
        stackTwo.pop()
        
        for x in tableCards:
            stackOne.insert(0,x)
            tableCards.remove(x)
        
        whoWins(playerOne, playerTwo)

    elif cardOne < cardTwo:
        tableCards.append(cardOne)
        tableCards.append(cardTwo)
        stackOne.pop()
        stackTwo.pop()

        for x in tableCards:
            stackTwo.insert(0,x)
            tableCards.remove(x)
            
        whoWins(playerOne, playerTwo)

    elif cardOne == cardTwo:
        tableCards.append(cardOne)
        tableCards.append(cardTwo)
        stackOne.pop()
        stackTwo.pop()

        for x in range(3):

            endGame(stackOne, stackTwo)
            
            cardOne = stackOne[-1]
            cardTwo = stackTwo[-1]
            tableCards.append(cardOne)
            tableCards.append(cardTwo)
            stackOne.pop()
            stackTwo.pop()


        whoWins(playerOne, playerTwo)
                
whoWins(playerOne, playerTwo)

    
    

    

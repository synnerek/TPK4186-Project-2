#from GameClass import Game
import ChessReader
import matplotlib.pyplot as plt
import StockfishGames
import OngoingGames

  

def StockfiskPlotter():
    StockfishGames.getStockfishGames()
    # x axis values
    x = ["Total wins", "Total drawn", "Total lost", "White wins", "White drawn", "White lost", "Black wins", "Black drawn", "Black lost"]
    # corresponding y axis values
    y = [StockfishGames.totalWins(), StockfishGames.totalDrawn(), StockfishGames.totalLost(), StockfishGames.winsWhite(), StockfishGames.drawnWhite(), StockfishGames.lostWhite(), StockfishGames.winsBlack(), StockfishGames.drawnBlack(), StockfishGames.lostBlack()]
    
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title("Stockfish's won, drawn and lost games in respectively total, white and black")

    # function to show the plot
    #plt.show()
    plt.savefig('StockfishGames.png', bbox_inches='tight')
    
    # function to show the plot
    plt.show()



def GamesStoppedAfterMovesPlotter():
    # x axis values
    maxMoves = OngoingGames.FindLongestGame()
    x = []
    for i in range(maxMoves):
        x.append(i+1)
    # corresponding y axis values
    y = OngoingGames.calculateMoves()
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title("Games who stopped at the given amount of moves")
    
    # function to show the plot
    #plt.show()
    plt.savefig('WhenGamesStopped.png', bbox_inches='tight')

def OngoingGamesAfterMovesPlotter():
    # x axis values
    maxMoves = OngoingGames.FindLongestGame()
    x = []
    for i in range(maxMoves):
        x.append(i)
    # corresponding y axis values
    total = OngoingGames.CalculateGamesStillOngoing('N')
    white = OngoingGames.CalculateGamesStillOngoing('W')
    black = OngoingGames.CalculateGamesStillOngoing('B')
    # plotting the points 
    plt.plot(x, total)
    plt.plot(x, white)
    plt.plot(x, black)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title("Ongoing games after a certain amount of moves")
    
    # function to show the plot
    #plt.show()
    plt.savefig('OngoingGames.png', bbox_inches='tight')


#StockfiskPlotter()
#GamesStoppedAfterMovesPlotter()
OngoingGamesAfterMovesPlotter()
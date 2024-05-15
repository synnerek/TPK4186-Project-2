from GameClass import Game
import ChessReader


name = "Stockfish"

def getStockfishGames():
    gameList = ChessReader.GetChessGameList("Stockfish.pgn")
    #print(Game.GetChessWhite(gameList[5]))
    stockfishList = []
    counter = 0
    for game in gameList:
        if (name in Game.GetChessWhite(game)) or (name in Game.GetChessBlack(game)):
            stockfishList.append(game)
            counter += 1
    return stockfishList

def totalWins():
    return winsWhite() + winsBlack()

def totalDrawn():
    return drawnWhite() + drawnBlack()

def totalLost():
    return lostBlack() + lostWhite()

def winsWhite():
    stockfishList = getStockfishGames()
    wins = 0
    for i in range(len(stockfishList)):
        if (name in str(Game.GetChessWhite(stockfishList[i]))) and (Game.GetChessResult(stockfishList[i]) == "1-0"):
            wins += 1
    return wins

def drawnWhite():
    stockfishList = getStockfishGames()
    drawn = 0
    for i in range(len(stockfishList)):
        if (name in Game.GetChessWhite(stockfishList[i])) and (Game.GetChessResult(stockfishList[i]) == "0-0"):
    #for game in stockfishList:
        #if (name in Game.GetChessWhite(game)) and (Game.GetChessResult(game) == "0 -0"):
            drawn += 1
    return drawn

def lostWhite():
    stockfishList = getStockfishGames()
    losses = 0
    for i in range(len(stockfishList)):
        if (name in Game.GetChessWhite(stockfishList[i])) and (Game.GetChessResult(stockfishList[i]) == "0-1"):
            losses += 1
    return losses

def winsBlack():
    stockfishList = getStockfishGames()
    wins = 0
    for i in range(len(stockfishList)):
        if (name in Game.GetChessBlack(stockfishList[i])) and (Game.GetChessResult(stockfishList[i]) == "0-1"):
            wins += 1
    return wins

def drawnBlack():
    stockfishList = getStockfishGames()
    drawn = 0
    for i in range(len(stockfishList)):
        if (name in Game.GetChessBlack(stockfishList[i])) and (Game.GetChessResult(stockfishList[i]) == "0-0"):
            drawn += 1
    return drawn

def lostBlack():
    stockfishList = getStockfishGames()
    losses = 0
    for i in range(len(stockfishList)):
        if (name in Game.GetChessBlack(stockfishList[i])) and (Game.GetChessResult(stockfishList[i]) == "1-0"):
            losses += 1
    return losses


getStockfishGames()

print(winsWhite())
print(winsBlack())
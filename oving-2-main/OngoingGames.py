import ChessReader
from GameClass import Game
import math


def FindLongestGame():
    gamelist = ChessReader.GetChessGameList("Stockfish.pgn")
    maxMoves = 0
    for i in range(len(gamelist)):
        if Game.GetNumberOfMoves(gamelist[i]) > maxMoves:
            maxMoves = Game.GetNumberOfMoves(gamelist[i])
    return maxMoves


def calculateMoves():
    # Listen angir hvor mange spill som fortsatt går. Plassen på elementet angir hvor mange trekk spillet er på, selve tallet på plassen angir hvor mange spill
    maxRounds = FindLongestGame()
    moves = []
    for i in range(maxRounds):
        moves.append(0)
    gamelist = ChessReader.GetChessGameList("Stockfish.pgn")
    for i in range(len(gamelist)):
        numberOfMoves = Game.GetNumberOfMoves(gamelist[i])
        amount = moves[numberOfMoves-1]
        moves[numberOfMoves-1] = amount + 1
    return moves


# Calculates all games still ongoing after a certain amount of moves
def CalculateGamesStillOngoing(Letter):
    moves = []
    maxRounds = FindLongestGame()
    games = ChessReader.GetChessGameList("Stockfish.pgn")
    for i in range(maxRounds):
            moves.append(0)
    if Letter == 'N':
        amountOfGames = len(games)
        for i in range(amountOfGames):
            numberOfMoves = Game.GetNumberOfMoves(games[i])
            amount = moves[numberOfMoves-1]
            moves[numberOfMoves-1] = amount + 1
        ongoingGames = []
        for i in range(maxRounds):
            ongoingGames.append(amountOfGames-moves[i])
            amountOfGames -= moves[i]
    elif Letter == 'W':
        for game in games:
            if ("Stockfish" in Game.GetChessWhite(game)):
                moves.append(Game.GetNumberOfMoves(game))
        lenGamesList = len(moves)
        print("W: ", lenGamesList)
        for i in range(lenGamesList):
            numberOfMoves = moves[i]
            amount = moves[numberOfMoves-1]
            moves[numberOfMoves-1] = amount + 1
        ongoingGames = []
        for i in range(maxRounds):
            ongoingGames.append(lenGamesList -moves[i])
            lenGamesList -= moves[i]
    elif Letter == 'B':
        for game in games:
            if ("Stockfish" in Game.GetChessBlack(game)):
                moves.append(Game.GetNumberOfMoves(game))
        lenGamesList = len(moves)
        print("B: ", lenGamesList)
        for i in range(lenGamesList):
            numberOfMoves = moves[i]
            amount = moves[numberOfMoves-1]
            moves[numberOfMoves-1] = amount + 1
        ongoingGames = []
        for i in range(maxRounds):
            ongoingGames.append(lenGamesList-moves[i])
            lenGamesList -= moves[i]
    return ongoingGames


# Mean deviations
# ----------
def MeanDeviation(Letter):
    gameList = ChessReader.GetChessGameList("Stockfish.pgn")
    numberOfMoves = 0
    numberOfGames = 0
    if Letter == 'N': # for normal mean deviation
        for game in gameList:
            numberOfMoves += Game.GetNumberOfMoves(game)
            numberOfGames += 1
    elif Letter == 'Wh': # for mean deviation in white games
        for game in gameList:
            if ("Stockfish" in Game.GetChessWhite(game)):
                numberOfMoves += Game.GetNumberOfMoves(game)
                numberOfGames += 1
    elif Letter == 'B': # for mean deviation in black games
        for game in gameList:
            if ("Stockfish" in Game.GetChessBlack(game)):
                numberOfMoves += Game.GetNumberOfMoves(game)
                numberOfGames += 1
    elif Letter == 'Wo': # for mean deviation in won games
        for game in gameList:
            if ((("Stockfish" in Game.GetChessBlack(game)) and (Game.GetChessResult(game) == '0 -1')) or (("Stockfish" in Game.GetChessWhite(game)) and (Game.GetChessResult(game) == '1 -0'))):
                numberOfMoves += Game.GetNumberOfMoves(game)
                numberOfGames += 1
    elif Letter == 'L': 
        for game in gameList:
            if ((("Stockfish" in Game.GetChessBlack(game)) and (Game.GetChessResult(game) == '1 -0')) or (("Stockfish" in Game.GetChessWhite(game)) and (Game.GetChessResult(game) == '0 -1'))):
                numberOfMoves += Game.GetNumberOfMoves(game)
                numberOfGames += 1
    return round(numberOfMoves/numberOfGames)



# Standard deviations. 
# -------------
# The function calculates one white move and one black move as one move in total
def StandardDeviation(Letter):
    gameList = ChessReader.GetChessGameList("Stockfish.pgn")
    numberOfMoves = []
    if Letter == 'N': # for normal standard deviation
        mean = MeanDeviation(Letter)
        for game in gameList:
            numberOfMoves.append(Game.GetNumberOfMoves(game))
    elif Letter == "B": # for black standard deviation
        mean = MeanDeviation(Letter)
        for game in gameList:
            if ("Stockfish" in Game.GetChessBlack(game)):
                numberOfMoves.append(Game.GetNumberOfMoves(game))
    elif Letter == 'Wh': # for white standard deviation
        mean = MeanDeviation(Letter)
        for game in gameList:
            if ("Stockfish" in Game.GetChessWhite(game)):
                numberOfMoves.append(Game.GetNumberOfMoves(game))
    '''
    elif Letter == 'Wo':
    elif Letter == 'L':
    '''
    numberOfMoves.sort()
    # First, calculate the deviations of each data point from the mean, and square the result of each
    deviations = 0
    for moves in numberOfMoves:
        deviations += (moves - mean)**2
    # The variance is the mean of these values
    variance = deviations/len(numberOfMoves)
    # and the population standard deviation is equal to the square root of the variance
    standardDev = math.sqrt(variance)
    return round(standardDev)

    
# print(FindLongestGame())
# print(calculateMoves())
#print(CalculateGamesStillOngoing())
#print(MeanDeviation())
#print(StandardDeviation('N'))

#print(calculateMoves())
#print(CalculateGamesStillOngoing('N'))
#print(CalculateGamesStillOngoing('B'))
#print(CalculateGamesStillOngoing('W'))
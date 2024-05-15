# 1. Imported Modules
# -------------------

from GameClass import Game
import re

# 2. Main
# -------


def GetChessGameList(inputFile):
    file = open(inputFile, "r")  # åpner filen
    line = file.readline()  # øverste linje i filen
    returnstring = ''

    while line:
        returnstring += line
        #line = file.readline()

    # returnerer en liste av strenger tilhørende et spill
    returnlist = returnstring.split("\n\n")
    returnlist.remove('')
    newlist = []

    for i in range(0, len(returnlist), 2):
        pair = [returnlist[i], returnlist[i+1]]
        newlist.append(pair)

    file.close()

    gamelist = []

    for element in newlist:
        newGame = Game(element)
        gamelist.append(newGame)

    return gamelist


def GetChessGameFromGameList(gamelist, event):
    for game in gamelist:
        gameevent = game.GetChessEvent()
        if gameevent == event:
            return game


def ChessGameToFile(filename, game):
    with open(filename, 'w') as file:
        moveCounter = 0
        file.write("[Event\t" + game.GetChessEvent() + "]\n")
        file.write("[Site\t" + game.GetChessSite() + "]\n")
        file.write("[Date\t" + game.GetChessDate() + "]\n")
        file.write("[Round\t" + game.GetChessRound() + "]\n")
        file.write("[White\t" + game.GetChessWhite() + "]\n")
        file.write("[Black\t" + game.GetChessBlack() + "]\n")
        file.write("[Result\t" + game.GetChessResult() + "]\n")
        file.write("[ECO\t" + game.GetChessEco() + "]\n")
        file.write("[Opening\t" + game.GetChessOpening() + "]\n")
        #file.write("[Variation\t" + game.GetChessVariation() + "]\n")
        file.write("[PlyCount\t" + game.GetChessPlyCount() + "]\n")
        file.write("[WhiteElo\t" + game.GetWhiteElo() + "]\n")
        file.write("[BlackElo\t" + game.GetBlackElo() + "]\n")
        file.write("\n")
        file.write(game.GetChessGamePlan() + "\n")


gamelist = GetChessGameList("Stockfish.pgn")
print(gamelist[1])
#ChessGameToFile("Stockfish.pgn", gamelist[0])

#print(gamelist[2].GetChessResult())
#print(Game.GetBlackMoves(gamelist[2]))
#print(Game.GetChessWhite(gamelist[5]))

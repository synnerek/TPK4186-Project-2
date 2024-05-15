
from pydoc import plain
import re

class Game:
    Event = None
    Site = None
    Date = None
    Round = None
    White = None
    Black = None
    Result = None
    eco = None
    Opening = None
    PlyCount = None
    WhiteElo = None
    BlackElo = None
    GamePlan = None

    gamedictionary = {}

    # det er ikke alle som har opening, så den må settes som standard med mindre den defineres som noe annet
    def __init__(self, list):
        stringlist = list[0].split('\n')
        self.Event = stringlist[0].split('"')[1]
        self.Site = stringlist[1].split('"')[1]
        self.Date = stringlist[2].split('"')[1]
        self.Round = stringlist[3].split('"')[1]
        self.White = stringlist[4].split('"')[1]
        self.Black = stringlist[5].split('"')[1]
        self.Result = stringlist[6].split('"')[1]
        self.eco = stringlist[7].split('"')[1]
        if (len(stringlist) == 12):
            self.Opening = stringlist[8].split('"')[1]
            self.PlyCount = stringlist[9].split('"')[1]
            self.WhiteElo = stringlist[10].split('"')[1]
            self.BlackElo = stringlist[11].split('"')[1]
        else:
            self.Opening = "standard"
            self.PlyCount = stringlist[8].split('"')[1]
            self.WhiteElo = stringlist[9].split('"')[1]
            self.BlackElo = stringlist[10].split('"')[1]
        # denne må vi fikse slik at den ikke har med tidene. Synne har koden for å ikke ha med det inne i klammeparantesene
        self.GamePlan = list[1].replace("\n", "")


    def __str__(self):
        returnstring = ''
        returnstring += "Event: "+ str(self.Event)+" \n"+ "Site: " + str(self.Site) + " \n"+ "Date: " + str(self.Date) + " \n"+ "Round: " + str(self.Round) + " \n"+ "White:" + str(self.White) + " \n"+ "Black:" + str(self.Black) + " \n"+ "Result:" + str(self.Result) + " \n"+ "ECO:" + str(self.eco) + " \n"+ "Opening:" + str(self.Opening) + " \n" + "Plycount:" + str(self.PlyCount) + " \n"+ "WhiteElo:" + str(self.WhiteElo) + " \n"+ "BlackElo:" + str(self.BlackElo)
        return returnstring

    def GetChessEvent(self):
        return self.Event
    
    def SetChessEvent(self, event):
        self.Event = event

    def GetChessSite(self):
        return self.Site

    def GetChessDate(self):
        return self.Date

    def GetChessRound(self):
        return self.Round

    def GetChessWhite(self):
        return self.White

    def GetChessBlack(self):
        return self.Black

    def GetChessResult(self):
        return self.Result

    def GetChessOpening(self):
        return self.Opening

    def GetChessEco(self):
        return self.eco

    def GetChessPlyCount(self):
        return self.PlyCount

    def GetChessWhiteElo(self):
        return self.WhiteElo

    def GetChessBlackElo(self):
        return self.BlackElo

    def GetChessGamePlan(self):
        return self.GamePlan

    def SeparateList(self):
        GameList = self.GamePlan
        Moves = []
        # Remove comments
        s = GameList.replace("\n", "")
        t = re.sub('{.*?}', '', s)
        # Creates a list of all moves
        AllMoves = re.split("\d+[.]", t)
        for el in AllMoves:
            if el == '':
                AllMoves.remove(el)
        for i in range(len(AllMoves)):
            newEl = AllMoves[i].strip(" ").split(" ")
            for move in newEl:
                if move == '':
                    newEl.remove(move)
            Moves.append(newEl)
        return Moves

    def GetAllMoves(self):
        self.SeparateList()

    def GetNumberOfMoves(self):
        return len(self.SeparateList())

    def GetWhiteMoves(self):
        WhiteMoves = []
        AllMoves = self.SeparateList()
        for move in AllMoves:
            WhiteMoves.append(move[0])
        return WhiteMoves

    def GetBlackMoves(self):
        BlackMoves = []
        AllMoves = self.SeparateList()
        for move in AllMoves:
            BlackMoves.append(move[1])
        return BlackMoves


class Move:
    def __init__(self, moveNumber, player, moveText):
        self.moveNumber = moveNumber
        self.player = player
        self.moveText = moveText

    def getMoveNumber(self):
        return self.moveNumber
    
    def getPlayer(self):
        return self.player
    
    def getMoveText(self):
        return self.moveText

    def __repr__(self):
        return f" Move Number: {self.moveNumber}, Move Text: {self.moveText}\n"


class Player:
    Name = None
    Rating = None

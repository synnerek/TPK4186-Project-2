import pandas as pd
from GameClass import Game, Move
import ChessReader


# Function that writes a game to an excelfile
def writeGame(game, filepath):
    data = {
        #"Move Number": [move.getMoveNumber() for move in game.getAllMoves()],
        #"Move": [move.getMoveText() for move in game.getAllMoves()],
        "Meta Data": ["Event: " + game.GetChessEvent(), 
                "Site: " + game.GetChessSite(), 
                "Date: " + game.GetChessDate(), 
                "Round: " + game.GetChessRound(), 
                "White: " + game.GetChessWhite(), 
                "Black: " + game.GetChessBlack(), 
                "Result: " + game.GetChessResult(), 
                "Eco: " + game.GetChessEco(), 
                "Opening: " + game.GetChessOpening(), 
                # hva er variation
                #"Variation: " + game.GetChessVariation(),
                "Plycount: " + game.GetChessPlyCount(), 
                "WhiteElo: " + game.GetChessWhiteElo(),
                "BlackElo: " + game.GetChessBlackElo()
                        ],
        #"Moves": ["Moves:" + str(game.GetAllMoves())]
                }
    # Må skrive alle moves til fil også
    '''
    for _ in range(0, data.get("Move Number").__len__() - data.get("Meta Data").__len__()):
        data.get("Meta Data").append("-")
        df = pd.DataFrame(data)
        df.to_excel(filepath, index= False)
    '''
    df = pd.DataFrame(data)
    df.to_excel(filepath, index=False)
    #game.getChessDataBase("Chess.pgn")



# Her er til å eventuelt gå gjennom en liste tror jeg, kanskje vi kan bruke det?
#for sheet_name in income_sheets.keys():
#    income_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)


# Function that reads a game from an excelfile
def readGame(file):
    
    df = pd.read_excel(file)
    gameList = df['Meta Data'].tolist()
    print(gameList)
    newGameList = []
    for el in gameList:
        newGameList.append(str(el.split(":")[1].strip(" ")))
    Event = newGameList[0]
    Site = newGameList[1]
    Date = newGameList[2]
    Round = newGameList[3]
    White = newGameList[4]
    Black = newGameList[5]
    Result = newGameList[6]
    eco = newGameList[7]
    if (len(newGameList) == 11):
        Opening = newGameList[8]
        PlyCount = newGameList[9]
        WhiteElo = newGameList[10]
        BlackElo = newGameList[11]
        #GamePlan = newGameList[12]
    else:
        Opening = "standard"
        PlyCount = newGameList[8]
        WhiteElo = newGameList[9]
        BlackElo = newGameList[10]
        #GamePlan = newGameList[11]
    print(game)
'''
        if move_count % 2 == 0:
            move = Chess.ChessMove(row["Move Number"], Chess.ChessPlayer(data_frame["Meta Data"][5], data_frame["Meta Data"][10]), row["Move"])
        else:
            move = Chess.ChessMove(row["Move Number"], Chess.ChessPlayer(data_frame["Meta Data"][6], data_frame["Meta Data"][11]), row["Move"])
        moves.append(move)  
                
    #newList = [event, site, date, round, white, black, result, eco, opening, plycount, moves]
    #print(newList)
    #return Game(newList)
    
    #game = pd.read_excel('./grades.xlsx') #<- legge inn riktig excelfil her
    #game.head()
'''


gamelist = ChessReader.GetChessGameList('Chess.pgn')
game = gamelist[0]
writeGame(game, "hi.xlsx")
readGame("hi.xlsx")


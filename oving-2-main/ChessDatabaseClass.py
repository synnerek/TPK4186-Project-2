from ChessReader import GetChessGame, GetGameEvent
from GameClass import Game

gameDictionary = {}
gamefile = ''


class ChessDatabase:

    def __init__(self, dictionary):
        self.gameDictionary = dictionary

    # Funksjon som lager en liste med strenger av hvert spill
    # Funksjon som gjør om listen til en liste av spill fra Game-klassen
    # Funksjoner for å legge til/fjerne games fra databasen
        # Må endre på både dictionaryen, men også filen

    def addGame(self, event):
        game = Game()
        thisgameevent = GetGameEvent(self.gamefile, event)
        self.gameDictionary[game] = GetChessGame(self.gamefile, event)

    # Da bør vi kanskje lage en funksjon for å skrive en ut fra dictionaryen og skrive om filen.

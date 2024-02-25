'''BoardClass class that creates a board for tic-tac-toe'''

class BoardClass():
    '''A class that makes up the public interface
    
    Attributes:
        Username of the main user
        Username of the opponent
        User name of the last player to have a turn
        Number of wins
        Number of ties
        Number of losses
    '''
    def __init__(self, 
                 User_name: str = "", 
                 Opponent_name: str = "", 
                 Recent_Player: str = "", 
                 Wins: int = 0, 
                 Ties: int = 0, 
                 Losses: int = 0,
                 Board: list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]) -> None:
        '''Making the gameboard.

        Args:
            Players user name
            User name of the last player to have a turn
            Number of wins
            Number of ties
            Number of losses
    '''
        self.User_name = User_name
        self.Opponent_name = Opponent_name
        self.setRecent_Player(Recent_Player)
        self.Wins = Wins
        self.Ties = Ties
        self.Losses = Losses
        self.Board = Board

    
    def setRecent_Player(self, Recent_Player: str) -> None:
        '''Sets the username of most recent player.
    
        Args:
            Username of the current player as a string.
        '''
        self.Recent_Player = Recent_Player
     
    def getRecent_player(self) -> str:
        '''Gets the recent player's name.
        
        Returns:
            The recent player's name.
        '''
        return self.Recent_Player
    def resetGameBoard(self) -> None:
        '''Clears the entire board.'''
        self.Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


    def updateGameBoard(self, move: int) -> bool:
        '''Updates the current board with a move given by the user.
        
        Args:
            An int from 1-9 indicating which square the player wants to fill in.
            
        '''
        try:
            move = int(move)
        except:
            return False
        
        empty_entries = 0
        game_end = False
        invalid_move = False
        for row in self.Board:
            empty_entries += row.count(" ")
        if empty_entries == 0:
            game_end = True
            self.Ties += 1
        if empty_entries % 2 == 0 and empty_entries != 0 and not game_end:
            if move in range(1, 10) and self.Board[(move - 1) // 3][(move % 3) - 1] == " ":
                self.Board[(move - 1) // 3][(move % 3) - 1] = "O"
            else:
                return False
        elif empty_entries % 2 == 1 and not game_end:
            if move in range(1, 10) and self.Board[(move - 1) // 3][(move % 3) - 1] == " ":
                self.Board[(move - 1 ) // 3][(move % 3) - 1] = "X"
            else:
                return False

        for rownum, row in enumerate(self.Board):
            print(f'{row[0]} | {row[1]} | {row[2]}')
            if rownum != 2:
                print("--|---|--")
            else:
                print()


        
    def isWinner(self) -> bool:
        '''Checks if there is a winner in the current board, and increases the wins of the player who won
        and increases the losses of the other player.
        
        Returns:
            True if there is a winner, false otherwise.
        
        '''
        for row in self.Board:
            if row[0] == row[1] == row[2] != " ":
                if self.Recent_Player == self.User_name:
                    self.Wins += 1
                else:
                    self.Losses += 1
                return True
            
        for column in range(3):
            if self.Board[0][column] == self.Board[1][column] == self.Board[2][column] != " ":
                if self.Recent_Player == self.User_name:
                    self.Wins += 1
                else:
                    self.Losses += 1
                return True
        
        if self.Board[0][0] == self.Board[1][1] == self.Board[2][2] != " " or self.Board[2][0] == self.Board[1][1] == self.Board[0][2] != " ":
            if self.Recent_Player == self.User_name:
                    self.Wins += 1
            else:
                    self.Losses += 1
            return True
            
        return False


    def boardIsFull(self) -> bool:
        '''Checks if the board is full.
        
        Returns:
            True if it is full, false otherwise.
        
        '''
        non_empty_entries = 0
        for row in self.Board:
            for entry in row:
                if entry != " ":
                    non_empty_entries += 1

        if non_empty_entries == 9:
            self.Ties += 1
            return True
        else:
            return False
        

    def printStats(self) -> None:
        '''Outputs the stats of the games played.'''
        print("------------------------------------------------------")
        print("Stats:")
        print(f"Your name: {self.User_name}")
        print(f"Total games played: {self.Wins + self.Losses + self.Ties}")
        print(f"Your wins: {self.Wins}")
        print(f"Your losses: {self.Losses}")
        print(f"Ties: {self.Ties}")
        print(f"Last person to make a move: {self.Recent_Player}")

    def getWins(self) -> int:
        '''Gets the amount of wins the current player has.
        
        Returns:
            An int representing the wins.
        '''
        return self.Wins
    
    def getLosses(self) -> int:
        '''Gets the amount of losses the current player has.
        
        Returns:
            An int representing the losses.
        '''
        return self.Losses
    
    def getTies(self) -> int:
        '''Gets the amount of ties.
        
        Returns:
            An int representing the ties.
        '''
        return self.Ties

    def getGamesPlayed(self) -> int:
        '''Gets the amount of games played.
        
        Returns:
            An int representing the amount of games played.
        '''
        return self.Ties + self.Losses + self.Wins




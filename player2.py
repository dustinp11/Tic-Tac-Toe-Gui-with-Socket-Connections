'''A class that creates the user-interface for tic-tac-toe.'''

import tkinter as tk
import gameboard
import socket
from tkinter import messagebox

class gameGUI:
    '''A user interface for player to play tic-tac-toe.
    
    Attributes: 
        socketobject: The socket object used to communicate between players.
        boardobject: The gameboard object that serves as the board.
        ipAddress: The IP address of the hosting player.
        server_port: The port of the hosting player.
        player_name: The username of the player.
        tkobject: Stores the tkinter object.
        frame: The frame object used to create the board.
        turn_number: The turn number, 0 indicates it is currently the first turn.
    '''
    boardobject = 0
    ipAddress = '0'
    server_port = 0
    user_name = ''
    opp_name = ''
    tkobject = 0
    frame = 0
    boardbuttons = []
    turn_number = 0
    #define variable functions 
    def __init__(self, player1or2) -> None:
        '''Make the ui.
        
        Args:
            Player1or2: 1 is the user is player 1, 2 otherwise.
        
        '''
        self.player1or2 = player1or2
        self.startCanvas()
        self.setMenu()
        self.createTitle()
        self.disablebuttons()


    def setGame(self) -> None:
        '''Creates the BoardClass object to be used to play the game.
        
        Args:
            The names of player1 and player2.
        '''
        self.boardobject = gameboard.BoardClass(User_name=self.user_name, Opponent_name=self.opp_name)

    def set_Socket(self, socketobject) -> None:
        '''Sets the socket object used to communicate with the other player.
        
        Args:
            The socket object.
        '''
        self.socketobject = socketobject



    def startCanvas(self) -> None:
        '''Starts the window for the game.'''
        self.tkobject = tk.Tk()
        self.tkobject.geometry('750x750')
        self.tkobject.configure(bg='#fab1b1')
        self.tkobject.title("Tic-Tac-Toe Game")

        self.tkobject.resizable(width=False, height=False)
        self.frame = tk.Frame(self.tkobject, height=200, width=200, bg='Grey')
        self.frame.place(x=55, y=130)
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text=' ', height=8, width=20, command=lambda i=i, j=j: self.updateButton(i*3 + j))
                button.grid(row=i, column=j)
                self.boardbuttons.append(button)
        
        self.disablebuttons()

    def disablebuttons(self) -> None:
        '''Disables all the buttons in the board.'''
        for button in self.boardbuttons:
                button.config(state=tk.DISABLED)
    
    def enableButtons(self) -> None:
        '''Enables all the buttons on the board.'''
        for button in self.boardbuttons:
                button.config(state=tk.NORMAL)
    
    def createTitle(self) -> None:
        '''Creates the title of the board.'''
        if self.player1or2 == 1:
            label = tk.Label(self.tkobject, text="Tic Tac Toe", font=('Arial', 30), bg='#bcd6f5')
        else:
            label = tk.Label(self.tkobject, text="Tic Tac Toe", font=('Arial', 30), bg='#fab1b1')
        label.place(height=100, width=500, relx=.04, rely=.01)

    def setMenu(self) -> None:
        '''Creates the menu for the player to pass information and their names into'''
        iptext = self.ipEntry()
        portentry = self.portEntry()
        username = self.usernameEntry()
        getinfobutton = tk.Button(self.tkobject, text='Listen', command=lambda: self.gethostinfo(iptext, portentry, username, getinfobutton))
        getinfobutton.place(x=230, y=670)
    

    def ipEntry(self) -> None:
        '''Creates the entry to enter in your ip address.'''
        iplabel = tk.Label(self.tkobject, text="Enter your ip address: ", font=('Arial', 13), bg='#f3c090')
        iplabel.place(height=20, width=180, x=65, y=555)
        iptext = tk.Entry(self.tkobject, width=50)
        iptext.config(state='normal')
        iptext.place(height=20,width=150, x=270, y=555)
        return iptext

    def portEntry(self) -> None:
        '''Creates the entry to enter in the port.'''
        port = tk.Label(self.tkobject, text="Enter your port: ", font=('Arial', 13), bg='#f3c090')
        port.place(height=20, width=180, x=65, y=585)
        portentry = tk.Entry(self.tkobject, width=50)
        portentry.config(state='normal')
        portentry.place(height=20,width=150, x=270, y=585)
        return portentry

    def usernameEntry(self) -> None:
        '''Creates the username entry to enter in your username.'''
        usernamelabel = tk.Label(self.tkobject, text="Enter your username: ", font=('Arial', 13), bg='#f3c090')
        usernamelabel.place(height=20, width=180, x=65, y=615)
        username = tk.Entry(self.tkobject, width=50)
        username.config(state='normal')
        username.place(height=20,width=150, x=270, y=615)
        return username

    def updateButton(self, position):
        '''Updates the board with the variable that corresponds with the move.'''
        if self.turn_number % 2 == 1:
            if self.boardbuttons[position]['text'] == ' ':
                self.boardbuttons[position]['text'] = 'O'
                move = str(position + 1)
                self.boardobject.updateGameBoard(move)
                self.boardobject.setRecent_Player(self.user_name)
                self.tkobject.after(300, self.socketobject.send(move.encode()))
                if not self.isGameEnd():
                    self.turn_number += 1
                    self.disablebuttons()
                    self.tkobject.after(300, self.player_receive_move)
        else:
            self.boardbuttons[position]['text'] = 'X'
            move = str(position + 1)
            self.boardobject.setRecent_Player(self.opp_name)
            self.boardobject.updateGameBoard(move)
            if not self.isGameEnd():
                self.turn_number += 1
                self.enableButtons()
    

    def StatsMenu(self) -> None:
        '''creates the menu which displays the stats.'''
        statsframe = tk.Frame(self.tkobject, height=200, width=350, bg='#f3c090')
        statsframe.place(x=530, y=133)
        opp_name = tk.Label(statsframe, text=f"Opponent Name: {self.opp_name}", font=('Arial', 13), bg='Grey')
        opp_name.grid(row=0, column=0, padx=10, pady=10)
        user_name = tk.Label(statsframe, text=f"User Name: {self.user_name}", font=('Arial', 13), bg='Grey')
        user_name.grid(row=1, column=0, padx=10, pady=10)
        wins = tk.Label(statsframe, text=f"Wins: {self.boardobject.getWins()}", font=('Arial', 13), bg='Grey')
        wins.grid(row=2, column=0, padx=10, pady=10)
        loss = tk.Label(statsframe, text=f"Losses: {self.boardobject.getLosses()}", font=('Arial', 13), bg='Grey')
        loss.grid(row=3, column=0, padx=10, pady=10)
        draw = tk.Label(statsframe, text=f"Draws: {self.boardobject.getTies()}", font=('Arial', 13), bg='Grey')
        draw.grid(row=4, column=0, padx=10, pady=10)
        gamesplayed = tk.Label(statsframe, text=f"Games Played: {self.boardobject.getGamesPlayed()}", font=('Arial', 13), bg='Grey')
        gamesplayed.grid(row=5, column=0, padx=10, pady=10)
    

    def gethostinfo(self, ipobject, portobject, usernameobject, infoobject) -> None:
        '''Receives the information from the textboxes created in setMenu, returns tuples with the address, port.
        
        Args:
            The object used to create the port entry, the username entry, and the button to submit.
        '''
        ipaddress = ipobject.get()
        port = portobject.get()
        username = usernameobject.get()
        ipobject.config(state=tk.DISABLED)
        portobject.config(state=tk.DISABLED)
        usernameobject.config(state=tk.DISABLED)
        infoobject.config(state=tk.DISABLED)
        try:
            infotuple = (ipaddress, int(port))
            self.user_name = username
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind(infotuple)
            serverSocket.listen()
            self.socketobject, clientAddress = serverSocket.accept()
            self.opp_name = self.socketobject.recv(1024).decode()
            self.socketobject.send(self.user_name.encode())
            self.setGame()
            self.tkobject.after(300, self.player_receive_move)
            self.StatsMenu()
        except:
            ipobject.config(state=tk.NORMAL)
            portobject.config(state=tk.NORMAL)
            usernameobject.config(state=tk.NORMAL)
            infoobject.config(state=tk.NORMAL)



    def resetAllButtons(self):
        for button in self.boardbuttons:
            button['text'] = ' '

   
    def isGameEnd(self) -> bool:
        '''When a button is clicked, this function should take in a move and update the board to reflect the current state.
        
        Returns:
            True if the game has ended.
        '''
        if self.boardobject.isWinner():
            winner = self.boardobject.getRecent_player()
            self.boardobject.resetGameBoard()
            self.resetAllButtons()
            self.turn_number = 0
            self.play_again()
            return True
        elif self.boardobject.boardIsFull():
            self.boardobject.resetGameBoard()
            self.resetAllButtons()
            self.turn_number = 0
            
            self.play_again()
            
            return True
        return False
    
    def play_again(self) -> None:
        '''Asks player1 if they want to play again, ends both programs if not.'''
        player1_response = self.socketobject.recv(1024).decode()
        if player1_response == "Play Again":
            self.StatsMenu()
            self.disablebuttons()
            self.tkobject.after(300, self.player_receive_move)
        else:
            self.StatsMenu()
            self.disablebuttons()


    def player_receive_move(self) -> str:
        '''Checks if a move has been recieved within .2 seconds, if not, nothing happens.
        
        Returns:
            The string that represents the move the other player made.
        '''
        move = self.socketobject.recv(1024).decode()
        self.updateButton(int(move) - 1)
        

    def runGame(self) -> None:
        '''Starts the mainloop to run the UI.'''
        self.tkobject.mainloop()


if __name__ == '__main__':
    gameGUI(2).runGame()
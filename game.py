# Game.py
#
# This module contains the classes and functions for running "games" in the
# game, whether if this is a single player or multi player game.

from gun import *

class Game():
    """ The main game class

    """
    def __init__(self,gametype):
        """ Variable gametype is a string that dictates the game type of the
            game (how it is going to end)

            Gametype is either "oneshot" (ends when someone gets shot) or
            "lastman" (ends when there is only one player left)

        """

        # For debugging purposes.
        print 'Game created!'
        print 'Game type is ' + gametype
        
        # Initialize an empty list of players playing the game.
        self.playerList = []

        # Set the gametype of the game.
        self.gametype = gametype

    def addPlayerToGame(player):
        """ This function adds a player into the list of players playing
            the game.
        """

        self.playerList.append(player)

        # Debugging message
        print player.name + ' has been added into the game!'

    def removePlayerFromGame(player):
        """ This function removes a player from the list of players in the
            game list.

            This can be used for many purposes, including but is not limited
            to removing players after they have died/lost.
        """
        try:
            self.playerList.remove(player)
            print 'Player ' + player.name + ' is out of the game!'
        except NameError:
            print 'Player ' + player.name + ' is an invalid player!'

    def start(self):
        """ The main function that handles the flow of a game.

        """
        # Get the number of max players
        self.maxPlayers = len(self.playerList)

        # A current player counter
        self.currentPlayer = 0

        # Create and initialize a gun, loaded with 1 bullet.
        gun = Gun()

        # DEBUG TODO: REMOVE THIS
        print len(self.playerList)

        # First we put it in a loop depending on the game type.
        
        # Oneshot game type
        if self.gametype == 'oneshot':
            # Add a bullet into the gun
            bullet = 1

            while bullet == 1: # Loop while nobody is shot yet
                if self.currentPlayer > self.maxPlayers - 1:
                    # Reset the counter if we have gone through the list
                    self.currentPlayer = 0
                print 'It is now ' + self.playerList[self.currentPlayer].name + '\'s turn!'

                # Ask the player to shoot themself.
                print self.playerList[self.currentPlayer].name + ', please press any key to shoot yourself.'
                raw_input()

                if gun.shoot() == 1:
                    # The current player has been shot!
                    bullet = 0

                    print self.playerList[self.currentPlayer].name + ' pulls the trigger.'
                    raw_input()

                    print 'BANG!'
                    print self.playerList[self.currentPlayer].name + ' has been shot!'
                    self.playerList[self.currentPlayer].alive = 0 # Mark the player as dead.

                    raw_input()

                else:
                    # It did nothing, give the gun to the next player.
                    print self.playerList[self.currentPlayer].name + ' pulls the trigger.'
                    raw_input()

                    print '*click*'
                    print self.playerList[self.currentPlayer].name + ' is still alive!'

                    if self.maxPlayers == 1: # If we only have one player
                        print self.playerList[self.currentPlayer].name + ' puts the gun against their head again.'

                    else: # We have more than one player
                        print self.playerList[self.currentPlayer].name + ' gives the gun to ' + self.playerList[self.currentPlayer].name + '.'

                    self.currentPlayer += 1 # Move the current player to the next
                    raw_input()

        elif self.gametype == 'lastman':
            # We need the game to loop while there is still more than 1 player.
            while len(self.playerList) > 1:
                if self.currentPlayer > self.maxPlayers:
                    # Reset the counter if we have gone through the list
                    self.currentPlayer = 1
                print 'It is now ' + self.playerList[self.currentPlayer].name + '\'s turn!'

                # Ask the player to shoot themself.
                print self.playerList[self.currentPlayer].name + ', please press any key to shoot yourself.'
                raw_input()

                print self.playerList[self.currentPlayer].name + ' pulls the trigger.'
                raw_input()

                if gun.shoot() == 1:
                    # The current player has been shot!
                    print 'BANG!'
                    print self.playerList[self.currentPlayer].name + ' has been shot and is out of the game!'
                    self.playerList[self.CurrentPlayer].alive = 0 # Mark the player as dead

                    # Now let's remove the player from the list
                    self.removePlayerFromGame(self.playerList[self.curentPlayer])

                    # We won't increment the current player because if the player has been shot and removed
                    # from the game, the next person in the list automatically takes his place.
                else:
                    # The player didn't get shot
                    print '*click*'
                    print self.playerList[self.currentPlayer].name + ' is still alive!'

                    print self.playerList[self.currentPlayer].name + ' gives the gun to ' + self.playerList[self.currentPlayer + 1].name + '.'
                    self.currentPlayer += 1 # Move the current player to the next
                    raw_input()

            # Now that the game is over, let's tell everyone who won
            print 'GAME OVER!'
            print self.playerList[1] + ' is the winner! Congratulations!'

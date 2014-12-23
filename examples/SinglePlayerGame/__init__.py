__author__ = 'thorsten'

# **********************************************************************************************************************
# Imports
# **********************************************************************************************************************
from ablauf import Automate
import examples.SinglePlayerGame.states

# **********************************************************************************************************************
# State diagramm
# **********************************************************************************************************************
#
# Start
# | (transition) init highscore
# Menu
# -> Options
# -> Highscore
# -> End
# |
# Game
# (leave function) enter highscore
# |
# Highscore
# |
# End


# **********************************************************************************************************************
# Ablauf initialization
# **********************************************************************************************************************
Automate.init()

Automate.setDebugMode(True) # Set Debug Level

# **********************************************************************************************************************
# Start Ablauf state engine
# **********************************************************************************************************************

# ----------------------------------------------------------------------------------------------------------------------
# Init function
# ----------------------------------------------------------------------------------------------------------------------
def initfunction():
    Automate.log("Process initfunction")
    Automate.log("-- Code would -> Initialize highscore")

# ----------------------------------------------------------------------------------------------------------------------
# Visit all states
# ----------------------------------------------------------------------------------------------------------------------

# At first, initializations are done and a menu will be  displayed
Automate.start("Menu",initfunction)

# in the menu you choose "Options" to change game parameter
Automate.transit("ShowOptions")

# in the options screen you finally choose "exit" and return to the menu screen
Automate.transit("BackToMenu")

# in the menu you choose "Highscores" to see all highscores scored so far
Automate.transit("ShowHighscores")

# in the highscores screen you choose "exit" and return to the menu screen
Automate.transit("BackToMenu")

# in the menu you choose "Start game" to play the game
Automate.transit("StartGame")

# after the game ends, a leaderboard with the scores will be displayed
Automate.transit("ShowHighscore")

# in the highscore screen you choose "exit" and return to the menu screen
Automate.transit("BackToMenu")

# in the menu you choose "quit game" to quit the game
Automate.transit("FinishFromMenu")
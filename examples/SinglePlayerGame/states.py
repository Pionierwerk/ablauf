__author__ = 'thorsten'

# **********************************************************************************************************************
# Imports
# **********************************************************************************************************************

from ablauf import Automate, State, Transition

# **********************************************************************************************************************
# Declare ablauf states
# **********************************************************************************************************************

# -----------------------------------------------------------------------------
# Menu state
# -----------------------------------------------------------------------------
Menu = State("Menu")

# Transition to Options
ShowOptions = Transition("ShowOptions", "Options", None)
Menu.addTransition(ShowOptions)

# Transition to Options
ShowHighscores = Transition("ShowHighscores", "Highscore", None)
Menu.addTransition(ShowHighscores)

# Transition to Game
StartGame = Transition("StartGame", "Game", None)
Menu.addTransition(StartGame)

# Transition to End
FinishFromMenu = Transition("FinishFromMenu", "End", None)
Menu.addTransition(FinishFromMenu)

# -----------------------------------------------------------------------------
# Options state
# -----------------------------------------------------------------------------
Options = State("Options")

# Transition to Menu
BackToMenu = Transition("BackToMenu", "Menu", None)
Options.addTransition(BackToMenu)

# -----------------------------------------------------------------------------
# Game state
# -----------------------------------------------------------------------------
Game = State("Game")

# Transition to Highscore
ShowHighscore = Transition("ShowHighscore", "Highscore", None)
Game.addTransition(ShowHighscore)


# Leave Function: put the highscore into the leaderboard
def GameLeaveFunction():
    Automate.log("Game leave function")
    Automate.log("-- Code would -> Put the highscore into the leaderboard")


Game.setLeaveFunction(GameLeaveFunction)

# -----------------------------------------------------------------------------
# Highscore state
# -----------------------------------------------------------------------------
Highscore = State("Highscore")

# Transition to Menu
GameOver = Transition("BackToMenu", "Menu", None)
Highscore.addTransition(GameOver)

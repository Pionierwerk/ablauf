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
stMenu = State("Menu")

# Transition to Options
tShowOptions = Transition("ShowOptions", "Options", None)
stMenu.addTransition(tShowOptions)

# Transition to Options
tShowHighscores = Transition("ShowHighscores", "Highscore", None)
stMenu.addTransition(tShowHighscores)

# Transition to Game
tStartGame = Transition("StartGame", "Game", None)
stMenu.addTransition(tStartGame)

# Transition to End
tFinishFromMenu = Transition("FinishFromMenu", "End", None)
stMenu.addTransition(tFinishFromMenu)

# -----------------------------------------------------------------------------
# Options state
# -----------------------------------------------------------------------------
stOptions = State("Options")

# Transition to Menu
tBackToMenu = Transition("BackToMenu", "Menu", None)
stOptions.addTransition(tBackToMenu)

# -----------------------------------------------------------------------------
# Game state
# -----------------------------------------------------------------------------
stGame = State("Game")

# Transition to Highscore
tShowHighscore = Transition("ShowHighscore", "Highscore", None)
stGame.addTransition(tShowHighscore)


# Leave Function: put the highscore into the leaderboard
def stGameLeaveFunction():
    Automate.log("Game leave function")
    Automate.log("-- Code would -> Put the highscore into the leaderboard")


stGame.setLeaveFunction(stGameLeaveFunction)

# -----------------------------------------------------------------------------
# Highscore state
# -----------------------------------------------------------------------------
stHighscore = State("Highscore")

# Transition to Menu
tGameOver = Transition("BackToMenu", "Menu", None)
stHighscore.addTransition(tGameOver)


from ablauf import State, Transition

# *************************************************************
# Declare Ncf states
# *************************************************************

# -------------------------------------------------------------
# Game State
# -------------------------------------------------------------
stState = State("State")

tFinishFromState = Transition("FinishFromState", "End", None)
stState.addTransition(tFinishFromState)
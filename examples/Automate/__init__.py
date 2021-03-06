__author__ = 'thorsten'

# **********************************************************************************************************************
# Imports
# **********************************************************************************************************************
import ablauf as abl
import examples.Automate.states

# **********************************************************************************************************************
# State diagramm
# **********************************************************************************************************************
#
# Start
# |
# State
# |
# End

# **********************************************************************************************************************
# Ablauf initialization
# **********************************************************************************************************************
abl.Automate.init()

abl.Automate.setDebugMode(True) # Set Debug Level

# **********************************************************************************************************************
# Start Ablauf state engine
# **********************************************************************************************************************
abl.Automate.start("State",None)
abl.Automate.transit("FinishFromState")
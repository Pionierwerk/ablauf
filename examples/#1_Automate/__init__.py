__author__ = 'thorsten'

import ablauf as abl
import states

# *************************************************************
# NonConForm initialization
# *************************************************************
abl.Automate.init()

# -------------- -----------------------------------------------
# Set Debug Level
# -------------------------------------------------------------
abl.Automate.setDebugMode(True)

# *************************************************************
# Start NonConForm state engine
# *************************************************************
abl.Automate.start("State")
abl.Automate.transit("FinishFromState")
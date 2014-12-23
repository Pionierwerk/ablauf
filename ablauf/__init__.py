# ----------------------------------------------------------------------------------------------------------------------
# The Automate module
# ----------------------------------------------------------------------------------------------------------------------
class Automate():
    """
    The functions of the automate are:

    * initialize the state engine
    * stores the states
    * trigger a transit from one state to another state via a transition
    """
    states = {}
    actualstate = None
    debugmode = False

    # ------------------------------------------------------------------------------------------------------------------
    # getter / setter
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    def getStates(self):
        """
        Returns the list of states

        :return: list of states
        :rtype: dict
        """
        return self.states


    @classmethod
    def getActualState(self):
        """
        Return the actual state of the automate

        :return: actual state
        :rtype: ablauf.state
        """
        return self.actualstate


    @classmethod
    def setActualState(self, state):
        """
        Set the actual state to a given state

        :param state: the new state
        :type state: ablauf.state
        """
        self.actualstate = state


    @classmethod
    def getDebugMode(self):
        """
        Return a boolean value to indicate if the debug mode is used

        :return: debug mode
        :rtype: boolean
        """
        return self.debugmode


    @classmethod
    def setDebugMode(self, mode):
        """
        Set the debug mode. Either to True or False

        :param mode: the new mode
        :type: boolean
        """
        self.debugmode = mode


    # ----------------------------------------------------------------------------------------------------------------------
    # functions
    # ----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def init(self):
        """
        Initialize Ablauf

        *Example:*

        .. code-block:: python

            from ablauf import Automate,State,Transition

            # -------------------------------------------------------------
            # Game State
            # -------------------------------------------------------------
            StartState = State("StartState")

            FinishFromState = Transition("FinishFromState", "End", None)
            StartState.addTransition(FinishFromState)

            # *************************************************************
            # Ablauf initialization
            # *************************************************************
            Automate.init()

            # -------------- -----------------------------------------------
            # Set Debug Level
            # -------------------------------------------------------------
            Automate.setDebugMode(True)

            # *************************************************************
            # Start Ablauf state engine
            # *************************************************************
            Automate.start("StartState")
            Automate.transit("FinishFromState")
        """

        self.log("initialize Ablauf")


    @classmethod
    def exit(self):
        """
        Exit the Ablauf State Engine
        """

        self.log("-----------------------------")
        self.log('finishing Ablauf')
        self.log("-----------------------------")


    @classmethod
    def addState(self, state):
        """
        Add a State to the list of states

        :param state: The new state that is added to the list of states
        :type state: ablauf.state
        """

        self.getStates()[state.getName()] = state


    @classmethod
    def getState(self, statename):
        """
        Get a state from the list of states

        :param statename: the name of the state
        :type statename: string
        :return: the state
        :rtype: ablauf.state
        """

        return self.getStates()[statename]


    @classmethod
    def transit(self, transitionname):
        """
        Do a transition to given state

        :param transitionname: the name of the new state
        :type transitionname: string
        """

        source = self.getActualState()
        transition = source.getTransition(transitionname)
        destination = self.getStates()[transition.getDestinationName()]

        if not source.leave is None:
            source.leave()

        self.log("|------------------Transit to------------------|:" + destination.getName())
        transition.fire()

        if not destination.enter is None:
            destination.enter()

        # Set new Stage & Controller & View function
        self.setActualState(destination)


    @classmethod
    def start(self, firststatename,initfunction):
        """
        starts the processing of the main loop

        *Example:*

        .. code-block:: python

            def initfunction():
                Automate.log("Processing init function")

            Automate.start("StartState",initfunction)

        :param firststatename: the name of the first state
        :type firststatename: string
        :param initfuction: the name of the function that is called during the transition from the Start state to the first state
        :type initfuction: function
        """
        _Start = State("Start")
        _GoFirst = Transition("GotoFirstState", firststatename, initfunction)

        _Start.addTransition(_GoFirst)

        _End = State("End")
        _End.setEnterFunction(self.exit)

        self.log("-----------------------------")
        self.log("start Ablauf state engine")
        self.log("-----------------------------")

        # set first state and transit to this stage
        self.setActualState(self.getState("Start"))
        self.transit("GotoFirstState")


    @classmethod
    def log(self, message):
        """
        Print a nessage to the console. If debugmode=true the message will be send to the javascript console.

        :param message: the message to print
        :type message: string
        """

        if self.getDebugMode() == True:
            print(message)


class State(object):
    """
    A defined state in the life cycle of a program. Could have a enter and a leaving function defined.

    *Example:*

    .. code-block:: python

        StartState = State("StartState")

        FinishFromState = Transition("FinishFromState", "End", None)
        StartState.addTransition(FinishFromState)

    :param name: the name of the state
    :type name: string
    """

    def defaultenterfunction(self):
        """
        The default enter function. If no enter function is defined, this function will be called. It do nothing, but log it's call
        """
        Automate.log("Entering:" + str(self.name))

    def defaultleavefunction(self):
        """
        The default leave function. If no leave function is defined, this function will be called. It do nothing, but log it's call
        """
        Automate.log("Leaving:" + str(self.name))

    def __init__(self, name):
        """
        A state inside the state engine.

        :param name: the name of the state
        :type name: string
        """
        self.name = name
        self.transitions = {}
        self.enterfunction = self.defaultenterfunction
        self.leavefunction = self.defaultleavefunction

        Automate.addState(self)


    def getName(self):
        """
        Get the name of the state

        :return: the name of the state
        :rtype: string
        """

        return self.name


    def enter(self):
        """
        Call the enter function. This will happen automatically when a transition to the state happens
        """

        self.enterfunction()

    def leave(self):
        """
        Call the leave function. This will happen automatically when a transition is triggered
        """

        self.leavefunction()

    def addTransition(self, transition):
        """
        Add a transition to the state.

        :param transition: the ransition to add
        :type transition: ablauf.Transition
        """

        self.transitions[transition.getName()] = transition

    def getTransition(self, transitionname):
        """
        Return the transition of the state with the given transition name

        :param transitionname: the name of the transition to get
        :type transitionname: string
        :return: the transition
        :rtype: ablauf.Transition
        """

        return self.transitions[transitionname]

    def setEnterFunction(self, enterfunction):
        """
        Set the enter function. This function will be called automatically when a transition to the state happens

        *Example:*

        .. code-block:: python

            def StateEnterFunction():
                Automate.log("Game enter function")

            StartState.setEnterFunction(StateEnterFunction)

        :param enterfunction: the enterfuncton
        """

        self.enterfunction = enterfunction

    def setLeaveFunction(self, leavefunction):
        """
        Set the leave function. This function will be called automaticaly when a transition formthe state happends

        *Example:*

        .. code-block:: python

            def StateLeaveFunction():
                Automate.log("Game leave function")

            StartState.setLeaveFunction(StateLeaveFunction)

        :param leavefunction: the leave function
        """

        self.leavefunction = leavefunction


class Transition(object):
    """
    A path from one state to another. It could have a transition function defined

    *Example:*

    .. code-block:: python

        def initfunction():
            Automate.log("Processing init function")

        _Start = State("Start")
        _GoFirst = Transition("GotoFirstState", firststatename, initfunction)

        _Start.addTransition(_GoFirst)

    :param name: Set the name of the new transition
    :type name: string
    :param destinationname: name of the destination state
    :type destinationname: string
    :param funct: The function that will be called when the transition is triggered
    :type funct: function
    """

    def __init__(self, name, destinationname, funct):
        """
        A transition inside the state engine.
        """

        self.name = name
        self.destinationname = destinationname
        self.funct = funct

    def getName(self):
        """
        Return the name of the transition

        :return: name The name of the transition
        :rtype: string
        """

        return self.name

    def getDestinationName(self):
        """
        Return the destination name of the transition

        :return: The destinationname of the transition
        :rtype: string
        """

        return self.destinationname

    def fire(self):
        """
        Calls the function of the transition

        """

        Automate.log("Firing transition function")
        if self.funct is not None:
            self.funct()
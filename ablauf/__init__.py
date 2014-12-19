__author__ = 'thorsten'

# ----------------------------------------------------------------------------------------------------------------------
# The #1_Automate module
# ----------------------------------------------------------------------------------------------------------------------
class Automate():
    states = {}
    actualstate = None
    debugmode = False

    # ------------------------------------------------------------------------------------------------------------------
    # getter / setter
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    def getStates(self):
        return self.states


    @classmethod
    def getActualState(self):
        return self.actualstate


    @classmethod
    def setActualState(self, state):
        self.actualstate = state


    @classmethod
    def getDebugMode(self):
        return self.debugmode


    @classmethod
    def setDebugMode(self, mode):
        self.debugmode = mode


    # ----------------------------------------------------------------------------------------------------------------------
    # functions
    # ----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def init(self):
        """
        A state machine

        *Example:*

        .. code-block:: python

            # -------------------------------------------------------------
            # Initialize #1_Automate
            # -------------------------------------------------------------
            non = ncf.ncfAutomate()

            # -------------------------------------------------------------
            # Start Stage
            # -------------------------------------------------------------
            ncf.ncfTransition('Finish','Exit')     # Transition to End Stage
            ncf.ncfStage(non)
            def Init(self):
                print "Stage Init"
                return self.nextStage("Finish")     # Continue with End Stage

            # -------------------------------------------------------------
            # End Stage
            # -------------------------------------------------------------
            ncf.ncfStage(non)
            def Exit(self):
                print "Stage Exit"
                ncf.exit()
                exit()

            # -------------------------------------------------------------
            # Start #1_Automate
            # -------------------------------------------------------------
            non.start("Init")                       # Start with the first Stage --> "Init"
        """

        self.log("initialize NonConForm")


    @classmethod
    def exit(self):
        """
        * Exit the NonConForm State Engine
        *
        * @method exit
        * @static
        """

        self.log("-----------------------------")
        self.log('finishing ablauf')
        self.log("-----------------------------")


    @classmethod
    def addState(self, state):
        """
        Add a State to the list of states

        @method addState
        @static
        @param {State} state The new state that is added to the list of states
        """

        self.getStates()[state.getName()] = state


    @classmethod
    def getState(self, statename):
        """
        Get a state from the list of states

        @method getState
        @static
        @param {string} statename the name of the state
        @return {State} the state
        """

        return self.getStates()[statename]


    @classmethod
    def transit(self, transitionname):
        """
        Do a transition to given state

        @method transit
        @static
        @param {string} transitionname the name of the new state
        """

        source = self.getActualState()
        transition = source.getTransition(transitionname)
        destination = self.getStates()[transition.getDestinationName()]

        if not source.leave is None:
            source.leave()

        self.log("|------------------Transit to------------------|:" + destination.getName())
        transition.fire()

        if not destination.enter is None:
            self.log("entering via function....")
            destination.enter()

        # Set new Stage & Controller & View function
        self.setActualState(destination)


    @classmethod
    def start(self, pFirststatename):
        """
        starts the processing of the main loop

        @method start
        @static
        """

        # compatibility with NonConForm JavaScript
        self.log("NonConForm main loop started")

        _stStart = State("Start")
        _tGoFirst = Transition("GotoFirstState", pFirststatename, None)
        _stStart.addTransition(_tGoFirst)

        _stEnd = State("End")
        _stEnd.setEnterFunction(self.exit)

        self.log("-----------------------------")
        self.log("start NonConForm state engine")
        self.log("-----------------------------")

        # set first state and transit to this stage
        self.setActualState(self.getState("Start"))
        self.transit("GotoFirstState")


    @classmethod
    def log(self, message):
        """
        Print a nessage to the console. If debugmode=true the message will be send to the javascript console.

        @method log
        @static
        @param message the message to print to the javascript console.
        """

        if self.getDebugMode() == True:
            print(message)


class State(object):
    def defaultenterfunction(self):
        Automate.log("Entering:" + str(self.name))

    def defaultleavefunction(self):
        Automate.log("Leaving:" + str(self.name))

    def __init__(self, name):
        """
        A state inside the state engine.

        @class State
        @constructor
        @param {string} name Set the name of the new state
        @example
        var stGame = new State("Game");<br/>
        var tFinishFromGame = new Transition("FinishFromGame","End",function() {});<br/>
        stGame.addTransition(tFinishFromGame);<br/>
        Ncf.addState(stGame);<br/>
        """
        self.name = name
        self.transitions = {}
        self.enterfunction = self.defaultenterfunction
        self.leavefunction = self.defaultleavefunction

        Automate.addState(self)


    def getName(self):
        """
        Get the name of the state

        @method getName
        @return {string} the name of the state
        """

        return self.name


    def enter(self):
        """
         Call the enter function. This will happen automaticaly when a transition to the state happenes

        @method enter
        """

        self.enterfunction()

    def leave(self):
        """
        Call the leave function. This will happen automaticaly when a transition away from the state happenes

        @method enter
        """

        self.leavefunction()

    def addTransition(self, transition):
        """
        Add a transition to the state.

        @method addTransition
        @param {Transition} transition
        """

        self.transitions[transition.getName()] = transition

    def getTransition(self, transitionname):
        """
        Return the transition of the state with the given transitionname

        @method getTransition
        @param {string} transitionname
        @return {Transition} the transition
        """

        return self.transitions[transitionname]

    def setEnterFunction(self, enterfunction):
        """
        Set the enter function. This function will be called automaticaly when a transition to the state happends

        @method setEnterFunction
        @param {function} enterfunction the enterfuncton
        """

        self.enterfunction = enterfunction

    def setLeaveFunction(self, leavefunction):
        """
        Set the leave function. This function will be called automaticaly when a transition formthe state happends

        @method setLeaveFunction
        @param {function} leavefunction the leave function
        """

        self.leavefunction = leavefunction

    def setModel(self, model):
        """
        Set the model. This model will be used for the actual view and controller in the main loop.

        @method setModel
        @param {dictionary} model the model
        """

        self.model = model

    def setController(self, controllerfunction):
        """
        Set the controller function. This function will be called automaticaly during the main loop, its the controller of a state.

        @method setController
        @param {function} controllerfunction the controller function
        """

        self.controllerfunction = controllerfunction


    def setView(self, viewfunction):
        """
        Set the view function. This function will be called automaticaly during the main loop, its the view of a state.

        @method setRunder
        @param {function} viewfunction the view function
        """

        self.viewfunction = viewfunction

    def getModel(self):
        """
        Return the model of the state

        @method getModel
        @return {dictionary} model the model
        """

        return self.model

    def getController(self):
        """
        Return the controller function of the state

        @method getController
        @return {function} controllerfunction the controller function
        """

        return self.controllerfunction

    def getView(self):
        """
        Return the view function of the state

        @method getView
        @return {function} viewfunction the view function
        """

        return self.viewfunction


class Transition(object):
    def __init__(self, name, destinationname, funct):
        """
        A transition inside the state engine.

        @class Transition
        @constructor
        @param {string} name Set the name of the new transition
        @param {string} name of the destination state
        @param {function} funct The function that will be called when the transition is triggered
        @example
        var stGame = new State("Game");<br/>
        var tFinishFromGame = new Transition("FinishFromGame","End",function() {});<br/>
        stGame.addTransition(tFinishFromGame);<br/>
        """

        self.name = name
        self.destinationname = destinationname
        self.funct = funct

    def getName(self):
        """
        Return the name of the transition

        @method getName
        @return {string} name The name of the transition
        """

        return self.name

    def getDestinationName(self):
        """
        Return the destination name of the transition

        @method getDestinationname
        @return {string} destinationname The destinationname of the transition
        """

        return self.destinationname

    def fire(self):
        """
        Calls the function of the transition

        @method fire
        """

        Automate.log("Firing transition function")
        if self.funct is not None:
            self.funct()
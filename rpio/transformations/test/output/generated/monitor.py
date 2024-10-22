# **********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
from rpio.clientLibraries.rpclpy.node import Node
from messages.messages import *


class monitor(Node):

    def __init__(self, config='config.yaml',verbose=False):
        super().__init__(config=config,verbose=verbose)

        self._name = "monitor"

    # ------------------------------------------------------------------------------------------------
    # -------------------------------------INTERNAL FUNCTIONS----------------------------------------
    # ------------------------------------------------------------------------------------------------
    def _SpinOnceFcn(self, args):

        # 0. RESET STATUS AND ACCURACY
        _success = True
        _accuracy = 1.0
        _status = "OK"

        # 1. FETCH KNOWLEDGE FROM KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT
        weatherConditions,weatherConditions_window = self.knowledge.read("weatherConditions",queueSize=1)
        shipPose,shipPose_window = self.knowledge.read("shipPose",queueSize=1)
        shipAction,shipAction_window = self.knowledge.read("shipAction",queueSize=1)

        # 2. PERFORM MONITORING VIA USER-SPECIFIC FUNTIONS OR SOFTWARE COMPONENTS (ORDERING!!!)


        # 2. PUT KNOWLEDGE IN KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT
        knowledge = predictedPath()
        knowledge._Confidence= "SET VALUE"    # datatype: Float_64
        knowledge._Waypoints= "SET VALUE"    # datatype: Float_32
        _success = self.knowledge.write(cls=knowledge)

        # 4. SIGNAL MONITORING STATE VIA KNOWLEDGE
        self.RaPSignalStatus(component=monitor,status=_status,accuracy=_accuracy)


        # (5) LOGGING DEMO
        self.logger.log("["+self._name+"] - "+"Monitoring property: "+weatherConditions.name +" with values:"+(1.0).__str__())
        self.logger.log("["+self._name+"] - "+"Monitoring property: "+shipPose.name +" with values:"+(1.0).__str__())
        self.logger.log("["+self._name+"] - "+"Monitoring property: "+shipAction.name +" with values:"+(1.0).__str__())

        # 4. return status of execution (fail = False, success = True)
        return _success

    def _EnterInitializationModeFcn(self):
        if self._verbose: print("["+self._name+"] - "+"Enter initializationModeFcn not implemented")

    def _ExitInitializationModeFcn(self):
        if self._verbose: print("["+self._name+"] - "+"Exit initializationModeFcn not implemented")

    def _EnterConfigurationModeFcn(self):
        if self._verbose: print("["+self._name+"] - "+"Enter configurationModeFcn not implemented")



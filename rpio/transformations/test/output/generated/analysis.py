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


class analysis(Node):

    def __init__(self, config='config.yaml',verbose=False):
        super().__init__(config=config,verbose=verbose)

        self._name = "analysis"

    # ------------------------------------------------------------------------------------------------
    # -------------------------------------INTERNAL FUNCTIONS----------------------------------------
    # ------------------------------------------------------------------------------------------------
    def _SpinOnceFcn(self, args):

        # 0. RESET STATUS AND ACCURACY
        _success = True
        _accuracy = 1.0
        _status = "OK"

        # 1. FETCH KNOWLEDGE FROM KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT
        pathEstimate,pathEstimate_window = self.knowledge.read("pathEstimate",queueSize=1)

        # 2. PERFORM MONITORING VIA USER-SPECIFIC FUNTIONS OR SOFTWARE COMPONENTS (ORDERING!!!)


        # 2. PUT KNOWLEDGE IN KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT
        knowledge = AnomalyMessage()
        knowledge._Anomaly= "SET VALUE"    # datatype: Boolean
        _success = self.knowledge.write(cls=knowledge)

        # 4. SIGNAL MONITORING STATE VIA KNOWLEDGE
        self.RaPSignalStatus(component=analysis,status=_status,accuracy=_accuracy)


        # (5) LOGGING DEMO
        self.logger.log("["+self._name+"] - "+"Monitoring property: "+pathEstimate.name +" with values:"+(1.0).__str__())

        # 4. return status of execution (fail = False, success = True)
        return _success

    def _EnterInitializationModeFcn(self):
        if self._verbose: print("["+self._name+"] - "+"Enter initializationModeFcn not implemented")

    def _ExitInitializationModeFcn(self):
        if self._verbose: print("["+self._name+"] - "+"Exit initializationModeFcn not implemented")

    def _EnterConfigurationModeFcn(self):
        if self._verbose: print("["+self._name+"] - "+"Enter configurationModeFcn not implemented")



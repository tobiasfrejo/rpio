# **********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
from rpio.clientLibraries.rpclpy.node import Node
from messages import *


class analysis(Node):

    def __init__(self, config='config.yaml',verbose=False):
        super().__init__(config=config,verbose=verbose)

        self._name = "analysis"
        self.logger.log("analysis instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR analyzeScanData-----------------------------
    def analyzeScanData(self):
        laserScan = self.knowledge.read("laserScan",queueSize=1)

        #TODO: ADD USER CODE FOR analyzeScanData


        knowledge = AnomalyMessage()
        knowledge._Anomaly= "SET VALUE"    # datatype: Boolean
        _success = self.knowledge.write(cls=knowledge)

        self.eventHandler.send(eventName='Anomaly')    # LINK <outport> Anomaly



    def register_callbacks(self):
        self.eventHandler.subscribe(eventName='laserScan', function=self.analyzeScanData)     # LINK <eventTrigger> laserScan

def main(args=None):

    node = analysis()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
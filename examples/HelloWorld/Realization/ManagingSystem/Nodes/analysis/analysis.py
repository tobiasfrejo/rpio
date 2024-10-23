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


class Analysis(Node):

    def __init__(self, config='config.yaml',verbose=False):
        super().__init__(config=config,verbose=verbose)

        self._name = "Analysis"
        self.logger.log("Analysis instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR analyse_scan_data-----------------------------
    def analyse_scan_data(self):
        laser_scan = self.knowledge.read("laser_scan",queueSize=1)

        #TODO: ADD USER CODE FOR analyse_scan_data


        knowledge = AnomalyMessage()
        knowledge._anomaly= "SET VALUE"    # datatype: Boolean
        _success = self.knowledge.write(cls=knowledge)

        self.eventHandler.send(eventName='anomaly')    # LINK <outport> anomaly



    def register_callbacks(self):
        self.eventHandler.subscribe(eventName='laser_scan', function=self.analyse_scan_data)     # LINK <eventTrigger> laser_scan

def main(args=None):

    node = Analysis()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
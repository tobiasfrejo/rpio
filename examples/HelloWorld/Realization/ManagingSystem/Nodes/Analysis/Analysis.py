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

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Analysis"
        self.logger.info("Analysis instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR analyse_scan_data-----------------------------
    def analyse_scan_data(self,msg):
        self.logger.info("analyse_scan_data executing...")
        laser_scan = self.knowledge.read("laser_scan",queueSize=1)

        #TODO: ADD USER CODE FOR analyse_scan_data



        self.publish_event(eventName='anomaly')    # LINK <outport> anomaly



    def register_callbacks(self):
        self.register_event_callback(eventName='new_data', function=self.analyse_scan_data)        # LINK <inport> new_data

def main(args=None):

    node = Analysis()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
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


class Monitor(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Monitor"
        self.logger.log("Monitor instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR monitor_data-----------------------------
    def monitor_data(self,msg):
        laser_scan = self.knowledge.read("laser_scan",queueSize=1)

        #TODO: ADD USER CODE FOR monitor_data






    def register_callbacks(self):
        self.register_event_callback(event_key='/Scan', callback=self.monitor_data)     # LINK <eventTrigger> /Scan
        self.register_event_callback(event_key='laser_scan', callback=self.monitor_data)        # LINK <inport> laser_scan

def main(args=None):

    node = Monitor()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
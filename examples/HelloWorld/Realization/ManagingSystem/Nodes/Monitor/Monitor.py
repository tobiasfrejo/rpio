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
        self.logger.log("monitor_data executing...")

        #TODO: ADD USER CODE FOR monitor_data


        knowledge = LaserScan()
        knowledge._ranges= "SET VALUE"    # datatype: array
        knowledge._angle_increment= "SET VALUE"    # datatype: Float_64
        _success = self.knowledge.write(cls=knowledge)

        self.publish_event(eventName='new_data')    # LINK <outport> new_data



    def register_callbacks(self):
        self.register_event_callback(eventName='scan', function=self.monitor_data)        # LINK <inport> scan

def main(args=None):

    node = Monitor()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
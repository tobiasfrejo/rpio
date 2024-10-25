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
#<!-- cc_include START--!>
# user includes here
#<!-- cc_include END--!>

#<!-- cc_code START--!>
# user code here
#<!-- cc_code END--!>

class Analysis(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Analysis"
        self.logger.log("Analysis instantiated")

    # -----------------------------AUTO-GEN SKELETON FOR analyse_scan_data-----------------------------
    def analyse_scan_data(self,msg):
        laser_scan = self.knowledge.read("laser_scan",queueSize=1)

        #<!-- cc_code_analyse_scan_data START--!>
        # user code here for analyse_scan_data
        #<!-- cc_code_analyse_scan_data END--!>

        knowledge = AnomalyMessage()
        knowledge._anomaly= "SET VALUE"    # datatype: Boolean
        _success = self.knowledge.write(cls=knowledge)

        self.publish_event(eventName='anomaly')    # LINK <outport> anomaly
    def register_callbacks(self):
        self.register_event_callback(event_key='laser_scan', callback=self.analyse_scan_data)     # LINK <eventTrigger> laser_scan

def main(args=None):

    node = Analysis()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
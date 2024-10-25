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

class Monitor(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Monitor"
        self.logger.info("Monitor instantiated")

        #<!-- cc_init START--!>
        # user includes here
        #<!-- cc_init END--!>

    # -----------------------------AUTO-GEN SKELETON FOR monitor_data-----------------------------
    def monitor_data(self,msg):
        laser_scan = self.knowledge.read("laser_scan",queueSize=1)

        #<!-- cc_code_monitor_data START--!>
        self.knowledge.write("laser_scan", msg)
        self.logger.info(f"new data arrived: {msg}")
        #<!-- cc_code_monitor_data END--!>


        self.publish_event(event_key='new_data')    # LINK <outport> new_data
    def register_callbacks(self):
        self.register_event_callback(event_key='Scan', callback=self.monitor_data)     # LINK <eventTrigger> Scan

def main(args=None):

    node = Monitor(config='config.yaml')
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
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
import time

class Monitor(Node):

    def __init__(self, config='config.yaml',verbose=False):
        super().__init__(config)

        self._name = "Monitor"
        self.logger.info("Monitor instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR monitor_data-----------------------------
    def monitor_data(self, payload):
        laser_scan = self.knowledge.read("laser_scan",queueSize=1)

        #TODO: ADD USER CODE FOR monitor_data






    def register_callbacks(self):
        self.event_handler.subscribe('/Scan', self.monitor_data)     # LINK <eventTrigger> /Scan
        self.event_handler.subscribe('laser_scan', self.monitor_data)        # LINK <inport> laser_scan

def main(args=None):

    node = Monitor("config.yaml")

    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
    try:

        print("Script is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Sleep to avoid busy-waiting
    except KeyboardInterrupt:
        print("\nKeyboard interruption detected. Exiting...")

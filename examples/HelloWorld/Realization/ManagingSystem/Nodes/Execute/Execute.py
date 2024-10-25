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
#<!-- cc_include START--!>
import json
import pickle
#<!-- cc_include END--!>

#<!-- cc_code START--!>
# user code here
#<!-- cc_code END--!>

class Execute(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Execute"
        self.logger.info("Execute instantiated")

        #<!-- cc_init START--!>
        # user includes here
        #<!-- cc_init END--!>

    # -----------------------------AUTO-GEN SKELETON FOR executer-----------------------------
    def executer(self,msg):
        isLegit = self.knowledge.read("isLegit",queueSize=1)
        directions = self.knowledge.read("direction",queueSize=1)

        #<!-- cc_code_executer START--!>
        self.event_handler.send('/spin_config', json.dumps(directions))

        # user code here for executer

        # self.publish_event(event_key='spin_config')  # LINK <outport> spin_config
        #<!-- cc_code_executer END--!>

    def register_callbacks(self):
        self.register_event_callback(event_key='new_plan', callback=self.executer)        # LINK <inport> new_plan
        self.register_event_callback(event_key='isLegit', callback=self.executer)        # LINK <inport> isLegit

def main(args=None):

    node = Execute(config='config.yaml')
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
    try:
       while True:
           time.sleep(1)
    except:
       exit()
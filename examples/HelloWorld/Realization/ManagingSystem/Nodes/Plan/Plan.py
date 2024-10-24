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


class Plan(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Plan"
        self.logger.log("Plan instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR planner-----------------------------
    def planner(self,msg):
        self.logger.log("planner executing...")
        Anomaly = self.knowledge.read("Anomaly",queueSize=1)

        #TODO: ADD USER CODE FOR planner


        knowledge = NewPlanMessage()
        knowledge._NewPlan= "SET VALUE"    # datatype: boolean
        _success = self.knowledge.write(cls=knowledge)

        self.publish_event(eventName='plan')    # LINK <outport> plan



    def register_callbacks(self):
        self.register_event_callback(eventName='Anomaly', function=self.planner)        # LINK <inport> Anomaly

def main(args=None):

    node = Plan()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
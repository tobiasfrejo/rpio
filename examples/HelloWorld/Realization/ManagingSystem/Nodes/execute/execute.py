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


class Execute(Node):

    def __init__(self, config='config.yaml',verbose=True):
        super().__init__(config=config,verbose=verbose)

        self._name = "Execute"
        self.logger.log("Execute instantiated")


    # -----------------------------AUTO-GEN SKELETON FOR executer-----------------------------
    def executer(self):
        isLegit = self.knowledge.read("isLegit",queueSize=1)

        #TODO: ADD USER CODE FOR executer


        knowledge = NewPlanMessage()
        knowledge._NewPlan= "SET VALUE"    # datatype: boolean
        _success = self.knowledge.write(cls=knowledge)
        knowledge = Direction()
        knowledge._omega= "SET VALUE"    # datatype: Float64
        knowledge._duration= "SET VALUE"    # datatype: Float64
        _success = self.knowledge.write(cls=knowledge)

        self.eventHandler.send(eventName='plan')    # LINK <outport> plan
        self.eventHandler.send(eventName='pathEstimate')    # LINK <outport> pathEstimate



    def register_callbacks(self):
        self.eventHandler.subscribe(eventName='isLegit', function=self.executer)        # LINK <inport> isLegit

def main(args=None):

    node = Execute()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
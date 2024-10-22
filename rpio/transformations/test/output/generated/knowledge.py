# **********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
from rpio.clientLibraries.rpclpy.node import Node
from messages.messages import *


class knowledge(Node):

    def __init__(self, config='config.yaml',verbose=False):
        super().__init__(config=config,verbose=verbose)

        self._name = "knowledge"
        self.logger.log("knowledge instantiated")

    # ------------------------------------------------------------------------------------------------
    # -------------------------------------INTERNAL FUNCTIONS----------------------------------------
    # ------------------------------------------------------------------------------------------------
    def _SpinOnceFcn(self, args):

        # 0. RESET STATUS AND ACCURACY
        _success = True
        _accuracy = 1.0
        _status = "OK"

        # 1. FETCH KNOWLEDGE FROM KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT

        # 2. PERFORM MONITORING VIA USER-SPECIFIC FUNTIONS OR SOFTWARE COMPONENTS (ORDERING!!!)


        # 2. PUT KNOWLEDGE IN KNOWLEDGE BASE VIA KNOWLEGE MANAGEMENT

        # 4. return status of execution (fail = False, success = True)
        return _success

    def register_callbacks(self):
        self.eventHandler.subscribe(eventName='event2', function=self.function1)
        self.eventHandler.subscribe(eventName='event3', function=self.function2)

def main(args=None):

    node = knowledge()
    node.register_callbacks()
    node.start()

if __name__ == '__main__':
    main()
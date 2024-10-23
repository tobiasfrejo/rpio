from array import array

from rpio.metamodels.aadl2_IL.aadl2_IL import *



def HelloWorld():
    #-----------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------- MESSAGES ----------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------


    #laserScan message
    ranges = data(name='ranges', dataType="array")
    angle_increment = data(name= 'angle_increment', dataType="Float_64")

    laserScan = message(name="laserScan",featureList=[ranges,angle_increment])

    # rotationAction message
    omega = data(name="omega",dataType="Float64")
    duration = data(name="duration",dataType="Float64")
    direction = message(name="direction",featureList=[omega,duration])

    # anomaly message
    Anomaly = data(name="Anomaly",dataType="Boolean")
    AnomalyMessage = message(name="AnomalyMessage",featureList=[Anomaly])

    newPlan = data(name="NewPlan",dataType="boolean")
    newPlanMessage = message(name="NewPlanMessage",featureList=[newPlan])

    # legitimate message
    Legitimate = data(name="legitimate",dataType="Boolean")
    legitimateMessage = message(name="legitimateMessage",featureList=[Legitimate])

    #-----------------------------------------------------------------------------------------------------------------------
    #--------------------------------------- LOGICAL ARCHITECTURE ----------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    adaptiveSystem = system(name="adaptiveSystem", description="Example adaptive system",messageList=[laserScan,direction,AnomalyMessage,newPlanMessage])

    #-A- --- managed system ---
    managedSystem = system(name="managedSystem", description="managed system part")

    laserScan_OUT = outport(name="laserScan",type="event data", message= laserScan)
    direction_IN = inport(name="direction",type="event data", message=direction)

    managedSystem.addFeature(laserScan_OUT)
    managedSystem.addFeature(direction_IN)

    #-B- --- managing system ---

    managingSystem = system(name="managingSystem", description="managing system part")

    laserScan_IN = inport(name="laserScan",type="event data", message=laserScan)
    direction_OUT = outport(name="direction",type="event data", message=direction)

    managingSystem.addFeature(laserScan_IN)
    managingSystem.addFeature(direction_OUT)

    # connections
    c1 = connection(source=laserScan_OUT, destination=laserScan_IN)
    c2 = connection(source=direction_OUT, destination=direction_IN)


    #---------------------COMPONENT LEVEL---------------------------

    #-MONITOR-
    monitor = process(name="monitor", description="monitor component")

    _laserScan = inport(name="laserScan",type="event data", message=laserScan)

    monitor.addFeature(_laserScan)


    #-ANALYSIS-
    analysis = process(name="analysis", description="analysis component")

    _laserScan = inport(name="laserScan",type="data", message=laserScan)
    _anomaly = outport(name="Anomaly",type="event data", message=AnomalyMessage)

    analysis.addFeature(_laserScan)
    analysis.addFeature(_anomaly)

    analyzeScanData = thread(name="analyzeScanData",featureList=[_laserScan,_anomaly],eventTrigger='laserScan')
    analysis.addThread(analyzeScanData)


    #-PLAN-
    plan = process(name="plan", description="plan component")

    #TODO: define input
    _anomaly_detected = inport(name="Anomaly",type="event data", message=AnomalyMessage)
    _plan = outport(name="plan",type="event data", message=newPlanMessage)

    plan.addFeature(_anomaly_detected)
    plan.addFeature(_plan)

    planner = thread(name="planner",featureList=[_anomaly_detected, _plan])
    plan.addThread(planner)

    #-LEGITIMATE-
    legitimate = process(name="legitimate", description="legitimate component")

    #-EXECUTE-
    execute = process(name="execute", description="execute component")

    _directionPlan = inport(name="plan",type="event data", message=direction)
    _isLegit = inport(name="isLegit",type="event data", message=legitimateMessage)
    _directions = outport(name="pathEstimate",type="event data", message=direction)

    execute.addFeature(_directionPlan)
    execute.addFeature(_isLegit)
    execute.addFeature(_directions)

    executer = thread(name="executer",featureList=[_plan,_isLegit,_directions])
    execute.addThread(executer)

    # #-KNOWLEDGE-
    # knowledge = process(name="knowledge", description="knowledge component")
    #
    # _weatherConditions = port(name="weatherConditions",type="event data", message=weatherConditions)
    # _shipPose = port(name="shipPose",type="event data", message=shipPose)
    # _shipAction = port(name="shipAction",type="event data", message=shipAction)
    # _pathEstimate = port(name="pathEstimate",type="event data", message=predictedPath)
    # _pathAnomaly = port(name="pathAnomaly",type="event data", message=AnomalyMessage)
    # _plan = port(name="plan",type="event data", message=predictedPath)
    # _isLegit = port(name="isLegit",type="event data", message=legitimateMessage)

    # knowledge.addFeature(_weatherConditions)
    # knowledge.addFeature(_shipPose)
    # knowledge.addFeature(_shipAction)
    # knowledge.addFeature(_pathEstimate)
    # knowledge.addFeature(_pathAnomaly)
    # knowledge.addFeature(_plan)
    # knowledge.addFeature(_isLegit)

    managingSystem.addProcess(monitor)
    managingSystem.addProcess(analysis)
    managingSystem.addProcess(plan)
    managingSystem.addProcess(legitimate)
    managingSystem.addProcess(execute)
    # managingSystem.addProcess(knowledge)

    #---------------------SYSTEM LEVEL---------------------------
    adaptiveSystem.addSystem(managingSystem)
    adaptiveSystem.addSystem(managedSystem)


    #-----------------------------------------------------------------------------------------------------------------------
    #--------------------------------------- PHYSICAL ARCHITECTURE ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------

    # XEON PROCESSOR CONNTECTION
    MIPSCapacity = characteristic(name="MIPSCapacity",value=1000.0,dataType="MIPS")
    I1 = port(name="I1",type="event data")
    XeonSolo = processor(name="Xeon",propertyList=[MIPSCapacity],featureList=[I1])


    # XEON PROCESSOR CONNTECTION
    MIPSCapacity = characteristic(name="MIPSCapacity",value=2000.0,dataType="MIPS")
    I2 = port(name="I2",type="event data")
    RPI = processor(name="Raspberry Pi 4B",propertyList=[MIPSCapacity],featureList=[I2])

    # WIFI CONNTECTION
    BandWidthCapacity = characteristic(name="BandWidthCapacity",value=100.0,dataType="Mbytesps")
    Protocol = characteristic(name="Protocol",value="MQTT",dataType="-")
    DataRate = characteristic(name="DataRate",value=100.0,dataType="Mbytesps")
    WriteLatency = characteristic(name="WriteLatency",value=4,dataType="Ms")
    interface = bus(name="interface",propertyList=[BandWidthCapacity,Protocol,DataRate,WriteLatency])

    interface.addConnection(I1)
    interface.addConnection(I2)

    return adaptiveSystem


    #-----------------------------------------------------------------------------------------------------------------------
    #--------------------------------------- MAPPING ARCHITECTURE ----------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------

HelloWorldDesign=HelloWorld()



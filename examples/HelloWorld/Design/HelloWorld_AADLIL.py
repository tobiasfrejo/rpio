from array import array

from rpio.metamodels.aadl2_IL.aadl2_IL import *



def HelloWorld():
    #-----------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------- MESSAGES ----------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------


    #laserScan message
    ranges = data(name='ranges', dataType="array")
    angle_increment = data(name= 'angle_increment', dataType="Float_64")

    laser_scan = message(name="LaserScan",featureList=[ranges,angle_increment])


    # rotationAction message
    omega = data(name="omega",dataType="Float64")
    duration = data(name="duration",dataType="Float64")
    direction = message(name="Direction",featureList=[omega,duration])

    # anomaly message
    anomaly = data(name="anomaly",dataType="Boolean")
    anomaly_message = message(name="AnomalyMessage",featureList=[anomaly])

    new_plan = data(name="NewPlan",dataType="boolean")
    new_plan_message = message(name="NewPlanMessage",featureList=[new_plan])

    # legitimate message
    legitimate = data(name="legitimate",dataType="Boolean")
    legitimate_message = message(name="LegitimateMessage",featureList=[legitimate])

    # new_data message
    new_data = data(name="new_data", dataType="Boolean")
    new_data_message = message(name="new_data_message", featureList=[new_data])



    #-----------------------------------------------------------------------------------------------------------------------
    #--------------------------------------- LOGICAL ARCHITECTURE ----------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    adaptiveSystem = system(name="adaptiveSystem", description="Example adaptive system",messageList=[laser_scan,direction,anomaly_message,new_plan_message,new_data_message])

    #-A- --- managed system ---
    managedSystem = system(name="managedSystem", description="managed system part")

    _laserScan_OUT = outport(name="laser_scan",type="event data", message= laser_scan)
    _direction_IN = inport(name="direction",type="event data", message=direction)

    managedSystem.addFeature(_laserScan_OUT)
    managedSystem.addFeature(_direction_IN)

    #-B- --- managing system ---

    managingSystem = system(name="managingSystem", description="managing system part")

    _laser_scan_IN = inport(name="laser_scan",type="event data", message=laser_scan)
    _direction_OUT = outport(name="direction",type="event data", message=direction)

    managingSystem.addFeature(_laser_scan_IN)
    managingSystem.addFeature(_direction_OUT)

    # connections
    c1 = connection(source=_laserScan_OUT, destination=_laser_scan_IN)
    c2 = connection(source=_direction_OUT, destination=_direction_IN)


    #---------------------COMPONENT LEVEL---------------------------

    #-MONITOR-
    monitor = process(name="Monitor", description="monitor component")

    _laserScan = inport(name="scan",type="event", message=laser_scan)
    _laserScanOut = outport(name="laser_scan", type="data", message=laser_scan)
    _new_data = outport(name="new_data", type="event", message=new_data_message)


    monitor.addFeature(_laserScan)

    monitor_data = thread(name="monitor_data",featureList=[_laserScan,_laserScanOut,_new_data])
    monitor.addThread(monitor_data)

    #-ANALYSIS-
    analysis = process(name="Analysis", description="analysis component")

    _new_data = inport(name="new_data", type="event", message=new_data_message)
    _laserScan = inport(name="laser_scan",type="data", message=laser_scan)
    _anomaly = outport(name="anomaly",type="event", message=anomaly_message)

    analysis.addFeature(_laserScan)
    analysis.addFeature(_anomaly)

    analyse_scan_data = thread(name="analyse_scan_data",featureList=[_laserScan,_anomaly,_new_data])
    analysis.addThread(analyse_scan_data)


    #-PLAN-
    plan = process(name="Plan", description="plan component")

    #TODO: define input
    _anomaly_detected = inport(name="Anomaly",type="event data", message=anomaly_message)
    _plan = outport(name="plan",type="event data", message=new_plan_message)

    plan.addFeature(_anomaly_detected)
    plan.addFeature(_plan)

    planner = thread(name="planner",featureList=[_anomaly_detected, _plan])
    plan.addThread(planner)

    #-LEGITIMATE-
    legitimate = process(name="Legitimate", description="legitimate component")

    #-EXECUTE-
    execute = process(name="Execute", description="execute component")

    _directionPlan = inport(name="plan",type="event data", message=direction)
    _isLegit = inport(name="isLegit",type="event data", message=legitimate_message)
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



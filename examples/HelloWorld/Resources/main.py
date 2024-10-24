from ManagingSystem.Nodes.monitor.monitor import Monitor
from ManagingSystem.Nodes.analysis.analyse import Analyse
from ManagingSystem.Nodes.plan.plan import Plan
from ManagingSystem.Nodes.execute.execute import Execute
import time 



monitor = Monitor("ManagingSystem/Nodes/monitor/config.yaml")
analyse = Analyse("ManagingSystem/Nodes/analysis/config.yaml")
plan = Plan("ManagingSystem/Nodes/plan/config.yaml")
execute = Execute("ManagingSystem/Nodes/execute/config.yaml")

monitor.register_callbacks()
analyse.register_callbacks()
plan.register_callbacks()
execute.register_callbacks()

monitor.start()
analyse.start()
plan.start()
execute.start()

try:
    print("Script is running. Press Ctrl+C to stop.")
    while True:
        time.sleep(1)  # Sleep to avoid busy-waiting
except KeyboardInterrupt:
    monitor.shutdown()
    analyse.shutdown()
    plan.shutdown()
    execute.shutdown()
    print("\nKeyboard interruption detected. Exiting...")
from rpio.utils.auxiliary import *


def launch(launchFile='launch.xml'):

    # 0. interpret launch file
    launchDescription = parse_launch_xml(file=launchFile,formalism="python")
    print(launchDescription)

    # 1. launch all commands at once
    execute_commands(extractCommands(launchDescription))


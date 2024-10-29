import pyLauncher

def launch(launchFile='launch.xml'):
    """Function to launch one or more python software component using a launch description file

    :param [launchFile]: [launch description file(XML)], defaults to [launch.xml]
    :type [launchFile]: [String](, optional)
    ...
    :return: [Functions returns nothing]
    :rtype: [None]
    """
    pyLauncher.launch(launchFile)

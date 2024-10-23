#**********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
from os import mkdir
from os.path import exists, dirname, join
import jinja2

def swc2code_py(system=None,path="output/generated"):

    if not exists(path):
        mkdir(path)

    # Initialize the Templates engine.
    this_folder = dirname(__file__)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

    # Load the template
    template = jinja_env.get_template('templates/swc_py.template')
    templateConfig = jinja_env.get_template('templates/swc_config.template')


    # Extract all processes from AADL system model
    for process in system.processes:

        # 0. Generate folder for each AADL process
        swcFolder = path + "/"+ process.name
        if not exists(swcFolder):
            mkdir(swcFolder)

        # 1. Generate code from AADL processes
        with open(join(swcFolder, process.name+".py"), 'w') as f:
            f.write(template.render(swc=process))

        # 2. Generate config.yaml file from AADL processes
        with open(join(swcFolder, "config.yaml"), 'w') as f:
            f.write(templateConfig.render(swc=process))

def message2code_py(system=None,path="output/generated/messages"):

    if not exists(path):
        mkdir(path)

    # Initialize the Templates engine.
    this_folder = dirname(__file__)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

    # Load the template
    template = jinja_env.get_template('templates/messages_py.template')

    # Extract all processes from AADL system model
    with open(join(path, "messages.py"), 'w') as f:
        f.write(template.render(messages=system.messages))


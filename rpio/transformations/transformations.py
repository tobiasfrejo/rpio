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

#-----------------------------------------------------------------------------------
#-----------------------------------AUXILIARY---------------------------------------
#-----------------------------------------------------------------------------------
def _AddRequirementsFile(file="requirements.txt", path=None):
    """Function to add a requirement.txt to the provided path."""

    # --- open file ---
    f = open(path + "/" + file, "a")

    # --- custom file content ---
    f.write("rpio==0.1.0\n")
    f.write("jsonpickle==3.3.0\n")
    f.write("paho-mqtt==2.1.0\n")
    f.write("PyYAML==6.0.2\n")


    # --- close file ---
    f.close()

def _AddDockerFile(file="Dockerfile",cmpName="", path=None):
    """Function to add a requirement.txt to the provided path."""

    # --- open file ---
    f = open(path + "/" + file, "a")

    # --- custom file content ---
    f.write("FROM python:3.10\n")
    f.write("ENV PYTHONUNBUFFERED 1\n")
    f.write("\n")
    f.write("ADD . c:/src/app\n")
    f.write("WORKDIR c:/src/app\n")
    f.write("ENV PYTHONPATH c:/src/app:$PYTHONPATH\n")
    f.write("\n")
    f.write("COPY requirements.txt ./\n")
    f.write("RUN pip3 install --no-cache-dir -r requirements.txt\n")
    f.write("\n")
    f.write("COPY config.yaml ./\n")
    f.write("COPY messages.py ./\n")
    f.write("COPY . .\n")
    f.write("\n")
    f.write('CMD ["python3", "'+cmpName+'.py"]\n')
    f.write("\n")

    # --- close file ---
    f.close()


#-----------------------------------------------------------------------------------
#--------------------------------TRANSFORMATIONS------------------------------------
#-----------------------------------------------------------------------------------
def swc2code_py(system=None,path="output/generated"):

    if not exists(path):
        mkdir(path)

    # Initialize the Templates engine.
    this_folder = dirname(__file__)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

    # Load the template
    template = jinja_env.get_template('templates/swc_py.template')
    templateConfig = jinja_env.get_template('templates/swc_config.template')
    templateMessages = jinja_env.get_template('templates/messages_py.template')


    # Extract all processes from AADL system model
    managingSystem = system.systems[0]
    for process in managingSystem.processes:

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

        # 3. Generate messages for standalone components
        with open(join(swcFolder, "messages.py"), 'w') as f:
            f.write(templateMessages.render(messages=system.messages))

        # 4. Add requirements.txt
        _AddRequirementsFile(path=swcFolder)

        # 5. Add Docker file
        _AddDockerFile(cmpName=process.name, path=swcFolder)



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






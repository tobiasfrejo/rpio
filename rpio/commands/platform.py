# Copyright (c) 2023-present Bert Van Acker (UA) <bert.vanacker@uantwerpen.be>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
from rpio.utils.auxiliary import *


@click.group()
@click.pass_context
def platformCmds():
    pass

@platformCmds.command()
@click.option('--verbose','-v', is_flag=True,default=False,help='Enable debug information.')
@click.option('--check', is_flag=True,default=False,help='Checking the prerequisites for running the adaptive application on this platform.')
@click.option('--set', is_flag=True,default=False,help='Setting up the prerequisites for running the adaptive application on this platform.')
@click.option('--force','-f', default='none', help='Force the setup of this platform [native, virtualenv, containerized].')
def platform(verbose,check,set,force):
    """Checking the prerequisites for running the adaptive application on this platform."""

    if check:
        if verbose:print("WARNING: platform check is not implemented yet.")

        # CHECK REDIS IS RUNNING
        REDIS_CHECK = check_redis(config=None)
        if REDIS_CHECK:
            print("INFO: REDIS connection check is successful.")
        else:
            print("ERROR: REDIS connection failed. Please check if the platform is connected to the host running the Redis")
            exit()

        #CHECK MQTT IS RUNNING
        MQTT_CHECK = check_mqtt(config=None)
        if MQTT_CHECK:
            print("INFO: MQTT connection check is successful.")
        else:
            print("ERROR: MQTT connection failed. Please check if the platform is connected to the host running the MQTT broker")
            exit()

    if set:
        if verbose: print("WARNING: platform setup is not implemented yet.")

        if force=="virtualenv":
            if verbose: print("INFO: Forcing to setup a virtual python environment for running the adaptive application on this platform.")
        elif force == "native":
            if verbose: print("INFO: Forcing to setup a native python environment for running the adaptive application on this platform.")
        elif force == "containerized":
            if verbose: print("INFO: Forcing to setup containerized environment for running the adaptive application on this platform.")


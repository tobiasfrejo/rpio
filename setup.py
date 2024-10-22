#**************************************************************************
# * Copyright (C) 2023-present Bert Van Acker (B.MKR) <bva.bmkr@gmail.com>
# * 
# * This file is part of the hybridIO project.
# * 
# * HybridIO can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# *************************************************************************

import platform
from setuptools import find_packages, setup

from rpio import (
    __author__,
    __description__,
    __email__,
    __license__,
    __title__,
    __version__,
    __url__
)

#--- insert platform dependent setup ---
#e.g., if platform.system() == "Darwin" and "arm" in platform.machine().lower():



setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=open("README.rst").read(),
    author=__author__,
    author_email=__email__,
    url=__url__,
    license=__license__,
    #install_requires=__install_requires__,
    python_requires=">=3.10",
    #packages=find_packages(include=["rpio", "rpio.*"]),
    entry_points={
        "console_scripts": [
            "rpio = rpio.__main__:main",
            "hio = rpio.__main__:main",
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        "DEVOPS",
        "FMI",
        "PLC",
        "XiL",
        "Model-based",
        "V&V automation",
    ],
)
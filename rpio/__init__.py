#**************************************************************************
# * Copyright (C) 2023-present Bert Van Acker (B.MKR) <bva.bmkr@gmail.com>
# *
# * This file is part of the hybridIO project.
# *
# * HybridIO can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# *************************************************************************

VERSION = (0, 0, "1-beta")
__version__ = ".".join([str(s) for s in VERSION])

__title__ = "rpio"
__description__ = (
    "HybridIO - your gateway to DEVOPS for mechatronic systems."
)
__url__ = "https://todo.org"

__author__ = "Bert Van Acker (B.MKR)"
__email__ = "bva.bmkr@gmail.com"

__license__ = "Closed-source"
__copyright__ = "Copyright 2023"

from .transformations import *
from .pyLauncher import *
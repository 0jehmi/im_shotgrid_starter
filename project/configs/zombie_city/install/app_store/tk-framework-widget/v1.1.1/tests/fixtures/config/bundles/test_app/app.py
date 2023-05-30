# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
A simple app to support unit tests.
"""

import sgtk


class TestApp(sgtk.platform.Application):
    """
    Dummy app that does nothing. It's sole purpose is so that
    it can request the use of the widget framework so we
    can access it from the tests. frameworks cannot be imported
    from outside an application bundle.
    """

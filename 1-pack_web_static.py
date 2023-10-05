#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive from the contents of the
we static folder of the AirBnB clone project.
The function used is:- def do_pack()
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Fabric script that contains a .tgz archive from
    the web static folder of the project"""
    local("sudo mkdir -p versions")
    date = datetime.utcnow()
    webfile = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                            date.month,
                                                            date.day,
                                                            date.hour,
                                                            date.minute,
                                                            date.second)
    result = local("sudo tar -cvzf {} web_static".format(webfile))
    if result.succeeded:
        return webfile
    if result.failed:
        return None

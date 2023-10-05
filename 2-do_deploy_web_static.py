#!/usr/bin/python3
"""
A fabric script based on 1-pack_web_static.py, that distributes the generated
.tgz archive to the respective web servers:- web-01 and web-02.
The function used is:- def do_deploy(archive_path)
"""

from datetime import datetime
from fabric.api import *
from os.path import exists

env.hosts = ['34.229.137.210', '3.90.85.167']


def do_deploy(archive_path):
    """A fabric script that distributes the .tgz archive file
    to the respective web servers"""

    if exists(archive_path) is False:
        return False

    webfile = archive_path.split("/")[-1]
    name = '/data/web_static/releases/' + "{}".format(webfile.split('.')[0])
    tmp = "/tmp/" + webfile

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(name))
        run("tar -xzf {} -C {}/".format(tmp, name))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(name, name))
        run("rm -rf {}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(name))
        return True
    except Exception:
        return False

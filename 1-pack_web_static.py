#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive
from the contents of the web_static
'''
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Path of archive or None on failure.
    '''
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    time_format = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{time_format}.tgz'
    archive_path = os.path.join('versions', archive_name)

    archive = local(f'tar -czvf {archive_path} web_static')

    if archive.failed:
        return None
    return archive_path

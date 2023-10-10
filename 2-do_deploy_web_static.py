#!/usr/bin/python3
'''
Fabric script to deploy web_static to web servers.
'''
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.164.87.125', '34.229.56.141']


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


def do_deploy(archive_path):
    """
    Deploys an archive to web servers.

    Args:
        archive_path (str):
            The path to the archive to deploy.

    Returns:
        bool:
            True if all operations were successful, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        name_no_ext = archive_name.split('.')[0]
        release_dir = f'/data/web_static/releases/{name_no_ext}'

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, f'/tmp/{archive_name}')

        # Uncompress the archive to the folder on the web server
        run(f'mkdir -p {release_dir}')
        run(f'tar -xzf /tmp/{archive_name} -C {release_dir}')

        # Delete the archive from the web server
        run(f'rm /tmp/{archive_name}')

        # Move files from web_static dir to the parent directory
        #run(f'mv {release_dir}/web_static/* {release_dir}/')
        run(f'rsync -av {release_dir}/web_static/* {release_dir}/')

        # Delete web_static directory
        run(f'rm -rf {release_dir}/web_static/')

        # Delete the symbolic link on the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link on the web server
        run(f'ln -s {release_dir} /data/web_static/current')

        print('--------------------------------------------------------')
        print(f'| {archive_name} deployed successfully! |')
        print('--------------------------------------------------------')
        return True

    except Exception as e:
        print(f'An error occurred: {e}')
        return False
    else:
        return True

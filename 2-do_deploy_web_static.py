#!/usr/bin/python3
'''
Fabric script to deploy web_static to web servers.
'''
import os
from fabric.api import *

env.hosts = ['54.164.87.125', '34.229.56.141']

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
        run(f'mv {release_dir}/web_static/* {release_dir}/')

        # Delete web_static directory
        run(f'rm -rf {release_dir}/web_static')

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

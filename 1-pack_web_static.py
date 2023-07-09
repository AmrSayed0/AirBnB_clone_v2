#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime

def do_pack():
    '''Generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")

    # Check if 'tar' command exists
    if local("which tar", capture=True).failed:
        print("Error: 'tar' command not found.")
        return None

    archive_name = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    archive_path = "versions/{}".format(archive_name)

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path

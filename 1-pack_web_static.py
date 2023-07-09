#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime

def do_pack():
    """Create a compressed archive from the web_static folder."""
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    archive_path = "versions/{}".format(archive_name)

    # Create versions folder if it doesn't exist
    local("mkdir -p versions")

    # Create the compressed archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None

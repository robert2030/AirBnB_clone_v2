#!/usr/bin/python3
"""script that generates a .tgz """
from fabric.api import local, hosts
from datetime import datetime
from fabric.contrib.files import exists
hosts_list = ['ubuntu@34.207.190.235', 'ubuntu@100.24.255.166']


@hosts(hosts_list)
def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        str: Archive path if successfully generated, None otherwise.
    """
    try:
        now = datetime.now()
        archive_name = "web_static_{}.tgz".format(now.strftime(
            "%Y%m%d%H%M%S"))

        if not exists("versions"):
            local("mkdir -p versions")

        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error packing archive:", e)
        return None

#!/usr/bin/python3
""" a module that generate an archive """
from fabric.api import local, run, put
from datetime import datetime


def do_pack():
    """ a function that compress file and stop them in an archive """
    try:
        time = datetime.now()
        timestamp = time.strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except Exception as e:
        return None

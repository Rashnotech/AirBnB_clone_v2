#!/usr/bin/python3
""" a module that generate an archive """
from fabric.api import local, run, put, env
from os import path
from datetime import datetime


env.hosts = ['rashnotech.tech', '54.162.47.71']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """ a function that deploy an archive to web servers
        Args:
            archive_path: file path
        Return:
            True otherwise False if the file path doesn't exit
    """
    if not path.isfile(archive_path):
        return False

    filename = path.basename(archive_path).split('.')[0]
    web_static = "/data/web_static"

    put(archive_path, "/tmp")
    run("mkdir -p {}/releases/{}".format(web_static, filename))
    run("tar -xzf /tmp/{} -C {}/releases/{}".format(filename + ".tgz",
                                                    web_static, filename))
    run("rm /tmp/{}".format(filename + ".tgz"))
    run("mv {}/releases/{}/web_static/* {}/releases/{}".format(web_static,
                                                               filename,
                                                               web_static,
                                                               filename))
    run("rm -rf {}/releases/{}/web_static".format(web_static, filename))
    run("rm -rf {}/current".format(web_static))
    run("ln -s {}/releases/{} {}/current".format(web_static,
                                                 filename, web_static))
    return True


def deploy():
    """ a function that deploy directly to the web servers """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)

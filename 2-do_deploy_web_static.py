#!/usr/bin/python3
""" a module that deploy an archive """
from fabric.api import local, run, put, env
from os import path


env.hosts = ['rashnotech.tech', '54.162.47.71']


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

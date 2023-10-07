#!/usr/bin/python3
"""a module that deletes out out of date archives """
import os
from fabric.api import run, local, env, lcd, cd


env.hosts = ["35.174.208.242", "54.162.47.71"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    """
    A function that delete all unecessaray archive
    Args:
      number: variable that keeps the most recent archives
    """

    number = int(number)
    if number == 0:
        number = 1

    archives = sorted(os.listdir("versions"))
    with lcd("versions"):
        to_delete = archives[:-number]
        for archive in to_delete:
            local("rm {}".format(archive))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        to_delete = [archive for archive in archives if 'web_static_' in
                     archive][:-number]
        for archive in to_delete:
            run("rm -rf {}".format(archive))

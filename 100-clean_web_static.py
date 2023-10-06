#!/usr/bin/python3
"""a module that deletes out out of date archives """
from fabric.api import local, cd, lcd, env
import os


env.hosts = ["rashnotech.tech", "54.162.47.71"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    A function that delete all unecessaray archive
    Args:
      number: variable that keeps the most recent archives
    """
    number = int(number)
    if number == 0:
        number = 1

    with lcd("versions"):
        archives = sorted(os.listdir("."))
        to_delete = archives[:-number]
        for achive in to_delete:
            local(f"rm {archive}")

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        to_delete = [archive for archive in archives if 'web_static_' in
                     archive][:-number]
        for archive in to_delete:
            run("rm -rf {}".format(archive))

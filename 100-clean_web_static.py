#!/usr/bin/python3
"""a module that deletes out out of date archives """
import os
from fabric.api import run, local, env, lcd, cd


env.hosts = ["35.174.208.242", "54.162.47.71"]
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
        print(number)

    archives = sorted(os.listdir("versions"))
    for i in range(number):
        archives.pop()
    with lcd("versions"):
        for arc in archives:
            local("rm {}".format(arc))

    with cd("/data/web_static/releases"):
        archieves = run("ls -tr").split()
        for arc in archieves:
            if "web_static_" in arc:
                archieves = arc
        archieves = list(archieves)
        for i in range(number):
            archieves.pop()
        for arc in archieves:
            run("rm -rf {}".format(arc))

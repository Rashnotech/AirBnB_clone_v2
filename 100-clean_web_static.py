#!/usr/bin/python3
"""a module that deletes out out of date archives """
from fabric.api import local, cd, lcd, env, run
import os


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

    archives = sorted(os.listdir("versions"))
    for _ in range(number):
        archives.pop()
    with lcd("versions"):
        for arc in archives:
            local("rm {}".format(arc))

    with cd("/data/web_static/releases"):
        archives = run("ls -ltr").split()
        for arc in archives:
            if "web_static_" in arc:
                archives = arc
        archives = list(archives)
        for _ in range(number):
            archives.pop()
        for arc in archives:
            run("rm -rf {}".format(arc))

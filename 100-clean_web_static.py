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
		for tar in archives:
local("rm {}".format(tar))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        for tar in archives:
            if 'web_static_' in tar:
                archives = tar
        archives = list(archives)
        for i in range(number):
            archives.pop()
        for tar in archives:
            run("rm -rf {}".format(tar))

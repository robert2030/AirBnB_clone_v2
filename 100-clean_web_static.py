#!/usr/bin/python3
"""
100-clean_web_static.py
This module contains a Fabric script that deletes
out-of-date archives, using the function do_clean
"""

from fabric.api import *
import datetime
import os

env.hosts = ['54.160.124.170', '52.205.97.123']
env.user = "ubuntu"
env.key_filename = "/alx-system_engineering-devops/\
0x04-loops_conditions_and_parsing/0-RSA_public_key"


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    files_ver = local("ls -t ./versions", capture=True).split("\n")
    files_rel = run("ls -t /data/web_static/releases/").split("\n")
    number = int(number)

    if files_ver:
        if number == 0 or number == 1:
            for i in range(1, len(files_ver)):
                local("rm versions/{}".format(files_ver[i]))
        else:
            for i in range(number, len(files_ver)):
                local("rm versions/{}".format(files_ver[i]))

    if files_rel:
        with cd("/data/web_static/releases/"):
            if number == 0 or number == 1:
                for i in range(1, len(files_rel)):
                    run("rm -r {}".format(files_rel[i]))
            else:
                for i in range(number, len(files_rel)):
                    run("rm -r {}".format(files_rel[i]))
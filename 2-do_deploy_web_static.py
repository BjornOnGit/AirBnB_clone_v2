#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['18.204.11.39', '54.90.56.2']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_exten = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'/format(path, no_exten))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_exten))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exten))
        run('rm -rf {}{}/web_static'.format(path, no_exten))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exten))
        return True
    except:
        return False
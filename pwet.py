#!/usr/bin/env python
from fabric.api import settings, run

def ps():
  with settings(host_string='root@192.168.0.1'):
    result = run("ps -ef|grep -i java|grep -v grep")
    print result
ps()

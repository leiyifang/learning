#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo


username="admin"
password="leiyifang123"

def ssh(ip,username,cmd):

    print(f'ssh {ip}, user:{username}, password:{password},execute:{cmd}')

ssh('192.168.1.1','python','show ver')



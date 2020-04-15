#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-04-16 01:51:32
# @Author  : bandit
# fork by giantbranch

# Whether to replace /bin/sh
REPLACE_BINSH = False

FLAG_BAK_FILENAME = "./copyfile/flags.txt"
PORT_INFO_FILENAME = "./copyfile/ports.txt"
PWN_BIN_PATH = "./bin"
XINETD_CONF_FILENAME = "./copyfile/pwn.xinetd"
PORT_LISTEN_START_FROM = 10000

XINETD = '''service ctf
{
    disable = no
    socket_type = stream
    protocol    = tcp
    wait        = no
    user        = root
    type        = UNLISTED
    port        = %d
    bind        = 0.0.0.0
    server      = /usr/sbin/chroot   
    server_args = --userspec=%s /home/%s ./run.sh %s
    # safety options
    per_source  = 10 # the maximum instances of this service per source IP address
    rlimit_cpu  = 20 # the maximum number of CPU seconds that the service may use
    rlimit_as  = 100M # the Address Space resource limit for the service
    #access_times = 2:00-9:00 12:00-24:00
}

'''

DOCKERFILE = '''FROM ubuntu

MAINTAINER Bandit

RUN sed -i 's/archive.ubuntu.com/asia-east1.gce.archive.ubuntu.com/g' /etc/apt/sources.list && apt update && apt-get install -y lib32z1 xinetd && rm -rf /var/lib/apt/lists/ && rm -rf /root/.cache && apt-get autoclean && rm -rf /tmp/* /var/lib/apt/* /var/cache/* /var/log/*
#apt update && apt-get install -y lib32z1 xinetd && rm -rf /var/lib/apt/lists/ && rm -rf /root/.cache && apt-get autoclean && rm -rf /tmp/* /var/lib/apt/* /var/cache/* /var/log/*

COPY ./'''+ XINETD_CONF_FILENAME +''' /etc/xinetd.d/pwn

COPY ./copyfile/service.sh /service.sh

RUN chmod +x /service.sh

# useradd and put flag
%s

# copy bin
%s

# creat run.sh
%s

# chown & chmod
%s

# copy lib,/bin 
%s

CMD ["/service.sh"]
'''

DOCKERCOMPOSE = '''version: '2'
services:
 pwn_deploy:
   image: pwn_deploy:latest
   build: .
   container_name: pwn_deploy
   ports:
    %s
'''


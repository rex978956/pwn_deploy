# pwn_deploy

A project for deploying ctf pwn challenge use chroot, fork from [pwn_deploy_chroot](https://github.com/giantbranch/pwn_deploy_chroot)

## Feature

1. Added timeout for pwn program
2. Modified by python3

## Before

```
# Install the latest version docker
curl -s https://get.docker.com/ | sh
# Install docker compose
apt install docker-compose
```

## How to use

```
1. Put your pwn program to ./bin （Note that the filename should not contain special characters.）
2. python3 initialize.py
3. docker-compose up --build -d     # please run as root
```

You can edit config.py to decide whether to replace /bin/sh with catflag

```
# Whether to replace /bin/sh

## replace
REPLACE_BINSH = True
## not replace(default)
REPLACE_BINSH = False
```

You can edit copyfile/run.sh to add instruction what you want to run.

```shell=
#!bin/sh
exec 2>/dev/null
timeout 120 ./$1
echo "\n\ntimeout"
```

## Attention

The flag will be generated by the initialize.py which store in flags.txt

The port information of the pwn program is also in the flags.txt.

## Update from fork

2019.04.15 version v1

## Reference

1. https://github.com/Eadom/ctf_xinetd
2. https://github.com/giantbranch/pwn_deploy_chroot

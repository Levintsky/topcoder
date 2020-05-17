# Linux Network

## Commands
- Curl:
```sh
curl -L google.com
```
- config network interface
```sh
ifconfig
```
- ping
```sh
ping 127.0.0.1 # ping self (should always work if net adaptor works)
```
- remote copy
```sh
rcp
scp local_file remote_username@remote_ip:remote_folder
```
- wget: retrieve web pages or files from http, https or ftp

## Remote Login
- Software: secureCRT, xShell, ...
- secure shell client
```sh
ssh usrname@192.168.x.x
```

## Get IP address, port
- Automatically get ip
- Static ip: /etc/sysconfig/network-scripts/ifcfg-eth0
- Check port
```sh
netstat -tunlp
```

## Domain
- DNS setup:
```sh
vi /etc/hosts
```
- Add following line to redirect baidu.com to specific;
```sh
xx.xx.xx.xx www.baidu.com
```

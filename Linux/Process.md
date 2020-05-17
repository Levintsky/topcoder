# Process

## Process Monitor
- ps:
```sh
ps -aux # check all, by user, bsd-style (must have a tty)
ps -aux | more
ps -aux | grep "python"
```
	- PID: process id;
	- TTY
	- TIME
	- CMD
	- STAT
	- ...
- Check parent (PPID):
```sh
ps -ef
pstree -p
pstree -u
```
- Kill/stop a process
```sh
kill -9 PID # kill a process force
killall sshd
pkill # kill a process
```

## Dynamic Monitor
- Process monitor:
```sh
top # check the status and usage of memory by processes
```
- Network monitor:
```sh
netstat
netstat -anp
```
- CPU:
```sh
gnome-system-monitor # to see cpu usage
```
- IO monitor
```sh
iotop
```
- jobs: list active jobs
- mpstat -P ALL; mpstat; #Process state

## Service Management
- Service operation:
```sh
service xxx [start|stop|restart|reload|status]
```
- Check system services: /etc/init.d/
- Check service status
```sh
chkconfig --list
```
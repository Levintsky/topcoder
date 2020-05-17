# Linux

## Basics
- Invented by Linus Torvalds:
	- Also create git;
- Version:
	- Ubuntu, RedHat, CentOS, Debian, Fedora, SuSE
	- All use Linux ad kernel;
- Unix:
	- IBM: AIX; Sun: Solaris; hp: hpux;
- Summary:\
	<img src="/Linux/linux.png" alt="drawing" width="400"/>
- Resources:
	- https://www.youtube.com/watch?v=4hUemuE_eU4&list=PLmOn9nNkQxJFYoQN9mBcr18fU1UAuWps0&index=1
- Virtual machine:
	- Bridge mode: host 192.168.14.100, then vm: 192.168.14.xxx;
		- Can visit each other (+); maybe ip conflict (-);
	- Nat mode: host 192.168.14.100, then vm could be 192.168.xx.xxx;
		- Less conflict (+); may not visit each other;
- Resources:
	- Linux Bash Commands: http://ss64.com/bash/
- Virtual machine: **virtual box**
	- guest-addition fix the resolution problem;

## Shutdown, reboot, login
- shutdown
```sh
shutdown -h now # shut down now
shutdown -h 1 # 1 min
shutdown -r now # reboot
halt # shutdown
```
- reboot
```sh
reboot
```
- Sync memory to disk;
```sh
sync
```

## User Management
- Change user
```sh
su # switch to root
su - usrname # switch to usrname, substitute user identity
sudo # switch user to do xxx
```
- Add user, change password
```sh
useradd [-d path] usrname # without -d will be /home/usrname as default
passwd usrname # change password
```
- Remove user:
```sh
userdel usrname # usrname will be deleted (not able to login), home folder kept
userdel -r usrname # also remove folder
```
- User info
```sh
id usrname
who # all logged in users
whoami # current username
```
- User with group
```sh
groupadd groupname
groupdel groupname
useradd [-g groupname] usrname
usermod -g group2 usrname # change user from original group to group2
```
- User info: /etc/passwd
- Group info: /etc/group
- Password info: /etc/shadow
- Switch running priority: check /etc/inittab
```sh
init 0/1/2/
```
- Get back root password:
	- Enter -> e -> 2nd-line (edit kernel) -> e -> 1 (single user) -> enter

## Misc
- Help
```sh
help
man make/rm/... # see the manual of xxx
```
- Execution:
	- .a files: static library
	- .so files: shared/dynamic library copy to /usr/lib
	- Can't find library in execution? vi /home/Levin/.bashrc; then change LD_LIBRARY_PATH;
	- Linux will not find .so files locally
- Output:
	- > and >>
	- tee: redirect output to multiple files, tee command is used to store and view (both at the same time) the output of any other command. Example: Paddle use following to print on both screen and an output file
```sh
cmd xxx 2>&1 | tee log
```
- History commands:
```sh
history
!178 # run 178 line
```
- Linux
```sh
lsb_release # check Linux release version
uname # print system information
```
- Change Access Management
```sh
# checkable by ls, e.g., (rwx), l (symlink), d (directory)
# u (owner), g (group) and o (other group); a all (ugo)
chmod # Change access
chmod o+x file
chmod a-x file
chown usrname file # Change owner:
ulimit # user limit
```

## Commands and Execution
- alias: alias m="ssh -X zhuoyuan@172.19.32.131"
- bash and sh: execute .sh in a subshell
- source and .: run in current shell
- exec: execute a program
- type: describe a command
- !!: run the last command again
- ###: #comment

## Compile
- make

## Dependency Check
- ldconfig:Configure Dynamic Linker Run Time Bindings. e.g., ldconfig /usr/local/cuda/lib64
- ldd ./calcflow: check dependency to see if we miss any .so files

## To Study
- comm
- install
- join:
- tr: change format; tr -s ’\textbackslash n’ < input.txt > output.txt;
- uniq: uniq < input.txt >output.txt

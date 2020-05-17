# SSH

## Resources
- https://zhuanlan.zhihu.com/p/21999778
- About key: https://zhuanlan.zhihu.com/p/108161141

## Basics
- Using ssh client, we can connect to ssh server:
```sh
ssh user@remote -p port # default port as 22
```
- If we can't connect, maybe remote has no ssh server installed:
```
local$ ssh user@remote -p port 
ssh: connect to host remote port 22: Connection refused
```
	- We can: sudo apt-get install openssh-server

## Password-Free
- Create a pair of keys (public, private) to generate a pair of xx_id_rsa and xx_id_rsa.pub
```sh
ssh-keygen
```
- Save private at local client, and copy the public at remote server
	- Copy the public key to the remote, save in authorized_keys.
```sh
ssh-copy-id user@remote -p port
ssh-copy-id xxx.pub user@remote
ssh user@remote -p port 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```
- Page local client side in .ssh/config:
```
Host lab
    HostName remote
    User user
    Port port
```
	- Example
```
Host zy_ubuntu
	User zhuoyuan
	Hostname 172.30.232.131
	Port 22
```
	- Another example
```
Host devfair
     User zhuoyuan
     Hostname 100.97.67.4
     Port 22
     ProxyJump prn-fairjmp03

Host *
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/fb_id_rsa
```

## SSH-Agent
- Start
```sh
ssh-agent $SHELL
eval `ssh-agent`
```
- Close
```sh
ssh-agent -k
```
- Add private key:
```sh
ssh-add ~/.ssh/key_name
```
- Check private key in proxy:
```sh
ssh-add -l # private
ssh-add -L # public
```
- Remove private key
```sh
ssh-add -d /path/of/key/key_name
ssh-add -D # remove all
```
- Summary:
```sh
# step 1: use any line below
ssh-agent bash
eval `ssh-agent`
# step 2: add private key to ssh-agent
ssh-add ~/.ssh/id_ras_test2
# step 3: log onto remote
ssh -i ~/.ssh/id_rsa_test2 root@x.x.x.x
exit
# step 4: this time no password required
ssh -i ~/.ssh/id_rsa_test2 root@x.x.x.x
```

## Remote File Transfer
```sh
# 把本地的 /path/to/local/file 文件传输到远程的 /path/to/remote/file
scp -P port /path/to/local/file user@remote:/path/to/remote/file

# 也可以使用别名
scp /path/to/local/file lab:/path/to/remote/file

# 把远程的 /path/to/remote/file 下载到本地的 /path/to/local/file
scp lab:/path/to/remote/file /path/to/local/file

# 远程的默认路径是家目录
# 下面命令把当前目录下的 file 传到远程的 ~/dir/file
scp file lab:dir/file

# 加上 -r 命令可以传送文件夹
# 下面命令可以把当前目录下的 dir 文件夹传到远程的家目录下
scp -r dir lab:

# 别忘了 . 可以用来指代当前目录
# 下面命令可以把远程的 ~/dir 目录下载到当前目录里面
scp -r lab:dir/ .
```

## Keep Program Running
- tmux: sudo apt-get install tmux;
```sh
tmux
tmux attach
```
- screen for Session Management
```sh
screen
screen -r
```

## Jump Machine
- E.g. 1: jumpbox
```sh
ssh -R 10022:localhost:22 jumpbox
ssh user@localhost -p 10022
```
	- ssh -R may disconnect? autossh for remedy:
```sh
autossh -NfR 10022:localhost:22 jumpbox
```

## Remote GUI
- Linux: X Server; Windows: Xming; Mac: XQuartz;
```sh
ssh -X remote
```

# Tools and Tricks to Work Remotely

## Remote
- 1. Connect VPN;
- 2. ssh;
```
ssh username@server
```
- 3. scp;

## Visualize
- 1. XQuartz: then visualized python will show in XQuartz;
```
ssh -X -a username@server
```
- 2. Code mount to local
```
sshfs username@server:/path-on-server/ ~/path-to-mount-point
sshfs zhuoyuan@172.30.232.131:/home/zhuoyuan/na/atg/experimental/rnd/3d-composition /Users/zhuoyuan/codes/code-remote
sshfs zhuoyuan@172.30.232.131:/home/zhuoyuan/experiments/python-opengl-tutorial /Users/zhuoyuan/codes/opengl-remote
```
	- In case of not responding, force kill:
```
pgrep -lf sshfs
kill -9 <pid_of_sshfs_process>
sudo umount -f <mounted_dir>
```
	- Or umount like following and remount;
```
sudo diskutil umount force /path/to/mount
```

## Remote Deskop
- Nomachine: install on both local and remote:
- Remote: .deb file for Ubuntu? https://www.nomachine.com/download/linux&id=1
```
sudo dkpg -i nomachine_xxx.deb
```
- Install on local (mac): https://www.nomachine.com/download/download&id=7

## Remote Interactive Python
- Run remote python
```
CUDA_VISIBLE_DEVICES=1 jupyter-notebook --port 8889 --ip 0.0.0.0 --no-browser
```
- Will produce something like:
```
[I 17:36:24.421 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 17:36:24.423 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/xxx/.local/share/jupyter/runtime/nbserver-xxx.html
    Or copy and paste one of these URLs:
        http://zhuoyuan-Tower:8889/?token=xxx
     or http://127.0.0.1:8889/?token=xxx
```
- Open browser, paste http://zhuoyuan-Tower:8889/?token=xxx 
# Docker

## Resources
- https://www.zhihu.com/search?type=content&q=docker
- https://zhuanlan.zhihu.com/p/23599229
- Official: https://docs.docker.com/

## Basics
- Concepts:
	- **Image**: a Ubuntu image is a template containing Ubuntu OS;
	- **Container**: a lightweight sandbox;
		- Used to run and separate apps;
	- **Repository**: places to put codes, files;
- Commands
```
docker version
```
- Operations on Docker image;
```
docker search [centos]
docker pull [centos]
docker images # now centos will show
```
- Operations on container:
```
docker run -it centos:latest /bin/bash # enter a new env
docker ps -a # /bin/bash will show
```
- Container to image:
```
docker commit -m "centos with git" -a "qixianhu" 72f1a8a0e394 xianhu/centos:git
```
- **Create image from Dockerfile**: https://docs.docker.com/engine/reference/builder/
```
# 说明该镜像以哪个镜像为基础
FROM centos:latest

# 构建者的基本信息
MAINTAINER xianhu

# 在build这个镜像时执行的操作
RUN yum update
RUN yum install -y git

# 拷贝本地文件到镜像中
COPY ./* /usr/share/gitdir/
```
	- Then we can build from Dockerfile:
	```
	docker build -t="xianhu/centos:gitdir" .
	```
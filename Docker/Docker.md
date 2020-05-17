# Docker

## Docker in Work
- Build, create and push an image to a docker registry in AWS, and be replicated to the kraken registry in IRN. This should also print the name of the image
```sh
bazel run --config=cuda push
```
- Launch the docker (if empty docker, just launch the host docker without the custorm-docker):
```sh
ma train tf docker \
  --command-line "/app/atg/experimental/rnd/mnist/train" \
  --zone irn-prod-gpus \
  --num-workers 1 \
  --num-gpus 1 \
  --num-cpus 8 \
  --memory-size-mb 60000 \
  --respool /Toronto \
  --mpi \
  --host-docker uber-usi/uber-caffe:xxxx \
  --custom-docker rna-toronto:xxxx-2020-01-16T01.30.39-00.00
```

## Resources
- https://www.zhihu.com/search?type=content&q=docker
- https://zhuanlan.zhihu.com/p/23599229
- https://zhuanlan.zhihu.com/p/89587030
- https://zhuanlan.zhihu.com/p/86351416
- Official: https://docs.docker.com/

## Basics
- Previously LXC (Linux Container);
- Docker:
	- Uses LXC for underlying implementation;
	- Makes processes sandbox-like (separate);
	- Implmented in go, supported by Apache2.0;
- Concepts:
	- **Image**: a Ubuntu image is a read-only template containing Ubuntu OS;
	- **Container**: a lightweight sandbox; an instance created from image;
		- Used to run and separate apps;
	- **Repository**: places to put codes, files;
		- Could be public and private; largest public is Docker Hub similar to git;
		- registry: similar to github service;
- Flexible, lightweight;
- Technology:
	- Namespace;
	- Control group;
- Main usage: build, ship, run;

## Usage Steps
- 1. Dockerfile
- 2. Build Dockerfile to Docker Image;
- 3. Run Docker container from Docker image;

## Commands
- Install:
```sh
yum install docker -y 
systemctl enable docker
systemctl start docker
```
- Misc:
```sh
docker version
docker info
```
- Operations on **Docker image**;
	```
	docker image ls [REPOSITORY[:TAG]]
	docker image pull NAME[:TAG]
	docker image push NAME[:TAG]
	docker image rm NAME[:TAG]
	docker image import file/URL/-[REPOSITORY[:TAG]]
	docker search IMAGE # search an image
	docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
	docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] # create an image from container
	```
	- Example:
	```
	docker search [nginx]
	docker pull [nginx]
	docker images # now centos will show
	docker save nginx >/tmp/nginx.tar.gz # 导出
	docker rmi -f nginx
	```
- Operations on container:
	```
	docker container ls [OPTIONS]
	docker container rm [OPTIONS] CONTAINER [CONTAINER...]
	docker container top CONTAINER [ps OPTIONS]
	docker container restart [OPTIONS] CONTAINER [CONTAINER...]
	```
	- Example
	```
	docker run -it centos:latest /bin/bash # enter a new env
	docker ps -a # /bin/bash will show
	```
- Container to image:
```sh
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
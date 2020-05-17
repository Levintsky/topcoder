# 0. try it fast
docker run hello-world

# 1. build, run and stop
cd node-bulletin-board/bulletin-board-app
docker build --tag bulletinboard:1.0 .
docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
docker rm --force bb

cd zy_test
docker build --tag zchen0211/mytest .
docker run -it zchen0211/mytest

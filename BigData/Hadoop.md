# Hadoop

## Resources
- https://zhuanlan.zhihu.com/p/20176725

## In-House
- Gateway Hosts:
```
ssh gw1-silver.pit-irn-1.uberatc.net
ssh gw2-silver.pit-irn-1.uberatc.net
```
- In gateway, you can
```
hadoop fs -ls /
hadoop fs -mkdir /user/zhuoyuan
```
- And a link like following can be found be ls
```
hdfs://ns-silver-prod-irn1/user/lmelinda/meshes/tor4d_v2/tor4d_v2_site/tor4d_v2_maps-tor4d_v2_eps/map_mesh
```
- Web UI:
```
http://nn1-silver.pit-irn-1.uberatc.net:50070/
http://nn2-silver.pit-irn-1.uberatc.net:50070/
```

## Install (Locally)
- Download:
```
wget https://archive.apache.org/dist/hadoop/common/hadoop-2.8.1/hadoop-2.8.1.tar.gz
tar xzf hadoop-2.8.1.tar.gz
```
- Change core-site.xml, hdfs-ste.xml
- Setup env (error libhdfs3 if not set correctly)
```
export HADOOP_INSTALL=~/hadoop-2.8.1
export HADOOP_HOME=$HADOOP_INSTALL
export PATH=$PATH:$HADOOP_INSTALL/bin
export CLASSPATH=$(hadoop classpath --glob)
```
- If get JAVA_HOME is not set error:
```
export JAVA_HOME=/opt/jdk/jdk1.8.0_141/
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
```
- Set ldconfig with JAVA_HOME
```
sudo bash -c "echo $JAVA_HOME/jre/lib/amd64/server >> /etc/ld.so.conf.d/hadoop.conf"
sudo ldconfig
```

## Use locally
- E.g.
```
hdfs dfs -ls /
hdfs dfs -ls /user/lmelinda/meshes/tor4d_v2/tor4d_v2_site/tor4d_v2_maps-tor4d_v2_eps/map_mesh
```
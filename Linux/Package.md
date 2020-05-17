# Install/Uninstall Package Management

- Search for and install software packages (Debian/Ubuntu)
```sh
apt-get:  
aptitude
```
- dpkg for package management:
```sh
- dpkg -l # list all packages
- dpkg -l | grep opencv
- dpkg -S # search a package
- dpkg -i xxx.deb # install a deb file
- sudo dpkg -r zip # uninstall a package
```

## Software
- Tool yum
```sh
yum list | grep xxx
yum install xxx # from yum server
```
- RPM (Redhad Package Manager);
```sh
cp xx.rpm /opt/ # generally put here
rpm -i package.rpm # install
rpm -e package # erase
rpm -e --nodeps foo # erase force
```

## Install from Source
To install a file (e.g. libpng): 
```sh
./configure # for settings)
make
sudo make install
```
- Things will be put in /usr/local/lib; /usr/local/include; /usr/local/bin;

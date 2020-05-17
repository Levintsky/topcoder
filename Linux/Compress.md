# Compression Tool

## gzip
- gzip and gunzip: compress and remove
```sh
gzip hello.txt # become hello.txt.gz
gunzip hello.txt.gz
```
- zip and unzip
```sh
zip -r abc.zip file1 directory2
unzip abc.zip [-d /path]
unzip -v abc.zip # just see what's inside without unzipping
```
- tar: compress and uncompress to .tar.gz
```sh
tar -zcvf file.tar.gz file1 file2 ... # compress
tar -zxvf file [-C /path] # extract(x) and display verbose(v) information from a
```
- bzip2: compress
- rar and unrar
- [gzipped(z)] file(f). -xvzf

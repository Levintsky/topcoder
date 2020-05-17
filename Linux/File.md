# Linux File System

## Basics
- Tree structured;
	- bin: binary;
	- dev: device;
	- etc: setup;
	- home:
	- lib, lib64;
	- media:
	- mnt:
	- opt:
	- root:
	- sbin:
	- selinux:
	- /proc, /srv, /sys: kernel (don't touch);
	- /tmp:
	- usr:
	- var:
- Everything is File;

## File and Folder Operation
```sh
cd
cp
diff -u old-file new file: compare files
find: e.g., find / -name ’libptf77blas.so’; to find a file
file: file type
mv #rename or move file
pwd # Display current path
rename
rm
rmdir # can't delete non-empty
touch
```
- Create multiple:
```sh
mkdir -p a/b/c # if a, b, c may not exist
```
- Symlink:
```sh
ln [OPTION] ... [-T] target link_name: make link
ln -s /webroot/home/httpd/test.com/index.php /home/vivek/index.php
```

## Display
- three related functions with regard to text files: displaying them, combining copies of them and creating new ones.
```sh
cat [-n] file # -n for line number
cat -n file | more # page by page
cat file1 > file2
more file
```
- For large file, page by page
```sh
less # one screen at a time
```
- Display
```sh
ls -l (details) -t(in time order) -r(reverse)
ls -f ./xxx/xx | wc -l # count how many files, -f: no sorting; wc -l: how many lines);
ls -a # all files, including .file)
ls -l | grep ’^{}-’ | wc -l # how many files)
ll xxx # check pseudo link
ls -l | grep ’^{}d’ | wc -l # how many folders)
ls -lR | grep ’^{}-’ | wc -l # how many files recursively)
ls /dev/disk/by-uuid [-l] # check uuid of disks:
```
- Echo, head and tail (for watch)
```sh
echo $PATH
echo "content" >> log.txt
head file # print first part
head -3 test.txt # print first 3 lines
head -n 3 test.txt # print first 3 lines
tail -3 test.txt # print last 3 lines
tail -f test.txt # actively watch changes
```
- stat: display status of the file
- xargs
- xrandr -o right/normal/left/invert: rotate display
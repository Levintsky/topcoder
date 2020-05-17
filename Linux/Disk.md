# Disk

## Disk Management Tool
```sh
baobab # Disk Utilize Analyzer: 
df -Th # check mounting status
du # Display folder size
```
- e.g. Check how many files
```sh
ls -l ./ | grep "^-" | wc -l # file start with -, folder start with d
```

## Partition
- Two types of partition: mbr (at most 4 primary parition), gtp (windows 7);
```sh
sudo fdisk -l: show the details
```
- Harddisk: IDE or SCSI
```sh
lsblk -f
```
- Partition in Linux by mount and umount
```sh
mount
umount
sudo mount -t ntfs /dev/sdb2 /media/DATA # actually mount the data
```
- Install a new disk and mount;
```sh
lsblk -f # check mount point
fdisk /dev/sdb # add a new partition
mkfs -t ext2 /dev/sdb1
mount /dev/sdb1 /home/xxx
```
- Mount automatically after reboot
	- Step 1: edit and add a new line
```sh
vi /etc/fstab # edit the path and uuid
```
```
/dev/sdb1 /home/xxx ext4 defaults 0 0
```
	- Step 2: Then mount
```sh
mount -a
```
	- Umount
```sh
umount /etc/sdb1
umount /home/xxx
```


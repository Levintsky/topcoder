# File Operation on AWS

## General
- Check AWS CLI: https://aws.amazon.com/cli/
```sh
aws s3 ls s3://mybucket
aws s3 cp myfolder s3://mybucket/myfolder --recursive
aws s3 sync myfolder s3://mybucket/myfolder --exclude *.tmp
```

## FB Version
- Setup
```ssh
module load fairusers_aws
```
- Basic Usage
	- Backup
```sh
fs3 backup /path/to/your/backup
```
	- List backups
```sh
fs3 ls /path/of/your/backup
```
	- Restore a file or a directory
```sh
fs3 restorefile /path/to/your/file
fs3 restoredir /path/to/your/dir/
```
	- Delete a file or a directory
```sh
fs3 purge /path/to/your/file
fs3 purge -r /path/to/your/dir/
```
- Directory
	- Personal (each user, replace user_name with your name): s3://fairusersglobal/users/user_name/
- Sync
	- One-by-one sync (Slower)
```sh
fs3cmd put /local/file s3://dl.fbaipublicfiles.com/minecraft2dvision/
```
	- Low-level sync (faster)
```sh
fs3cmd sync -p /local/folder s3://dl.fbaipublicfiles.com/minecraft2dvision/
```
Then your folder will be available at https://dl.fbaipublicfiles.com/minecraft2dvision/
- Low-level delete
```
fs3cmd del s3://fairusersglobal/users/maj/h1/checkpoint/maj/unneeded.txt
```
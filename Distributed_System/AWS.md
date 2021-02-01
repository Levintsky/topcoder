# File Operation on AWS

## General
- Amazon S3 = Amazon Simple Storage Service
- 5 main functions:
	- Create
	- Store up to 5T
	- Download
	- Access
	- Standard REST and SOAP api;
- Introduction: https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/Introduction.html
- Price: https://aws.amazon.com/s3/pricing/
	- Around 0.02 usd per GB;
- Concepts:
	- Bucket: a container to save objects;
		- Highest level s3 namespace;
		- Identify store/transfer account;
- Configure credential and configure file:
```
~/.aws/credentials
~/.aws/config
```
- Check AWS CLI: https://aws.amazon.com/cli/
```sh
aws s3 ls s3://mybucket
aws s3 cp myfolder s3://mybucket/myfolder --recursive
aws s3 sync myfolder s3://mybucket/myfolder --exclude *.tmp
```

## Making requests
- Access key: 20-char;
- Secret access key: 40-char;
- AWS Identity and Access Management (IAM)
- 1. Making requests by ipv6;
- 2. Making requests by AWS SDK:
```
# ~/.aws
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```
- 3. Making requests with REST API

## Bucket
- Create a bucket
	- Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/.
	- Choose Create bucket.
	- In Bucket name, enter a DNS-compliant name for your bucket. The bucket name must:
		- Be unique across all of Amazon S3.
		- Be between 3 and 63 characters long.
		- Not contain uppercase characters.
		- Start with a lowercase letter or number.
- Delete a bucket:
```sh
aws s3 rb s3://bucket-name --force
aws s3 rm s3://bucket-name --recursive
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
# Linux Shell

## Basics
- A language provided to operate Linux kernel;
	- Similar as python; (python is more powerful);
- Check all valid interpreter:
```sh
cat /etc/shells
echo $SHELL # check default
```
- Available:
```sh
/bin/sh
/bin/bash
/bin/rbash
/bin/dash
/usr/bin/screen
```

## Write a shell
- Specify interpreter (otherwise default):
```
#!/bin/bash
```
- Execute
```sh
sh xxx.sh
bash xxx.sh
./xxx.sh # need executable access!
```

## Variable
- System var:
```sh
$HOME
$PWD
$SHELL
$USER
```
- User defined: no space!!! always as string!
```sh
A=1
echo $A
unset A
readonly B=3 # static
unset B # can't unset!
A=1+1
echo $A # 1+1, not 2
A="a b ccc"
```
- Global variable
```sh
export D
export D=abc
```
- Special variable:
```sh
$n # $1, $2, ..., $9, ${10}
echo "$1 $2"
$0 # Stores the first word of the entered command (the name of the shell program).
```
- Special
```sh
$# # Number of all arguments
$* # All the arguments that were entered on the command line ($1 $2 ...).
$@ # All the arguments that were entered on the command line,
$? # The exit value of the last command that was executed.
```
- Numerical expression:
```sh
expr 3 + 2
expr `expr 2 + 3` \* 4
s=$[(2+3)*4]
```
- Condition
```sh
[ 23 -ge 22 ]
echo $?
[ -e file ] # exist?
[ -w file ] # writable?
```

## Condition
- Method 1:
```sh
if [ exp... ];then
	program
fi
```
- Method 2:
```sh
if [ xxx... ]
then
	program
elif [ xxx ]
then
	program
fi
```

## Loop
- For loop
```sh
s=0
for((i=1;i<=100;i++))
do
	s=$[$s+$i]
done
```
- While loop: check code

## Common commands
- Cut
```sh
cut -d " " -f 1 cut.txt # 1st column
cut -d " " -f 2,3 cut.txt # 2, 3 column
echo $PATH | cut -d : -f 3-
```
- Sed: stream edit (insert, remove, edit)
```sh
sed
sed "2a xxxx" file.txt # insert xxxx after the 2nd line
sed "2d" file.txt # delete 2nd line
sed "/xxxx/d" file.txt # remove xxxx
sed "s/xxx1/xxx2/g" file.txt # replace xxx1 with xxx2
sed -e "2d" -e "s/xx1/xx2/g" file.txt # multiple operation
```
- awk:  Find and Replace text, database sort/validate/index
- gawk: find and replaces within files
```sh
awk [opt] 'pattern1 {action1} pattern2 {action2}'
awk -F : '/^root/ {print $7}' file
```
- Sort
```sh
sort
sort -k 2,2 input.txt >output.txt
```

## Interview Questions
- Check line number of empty lines in file1:
```sh
awk '/^$/{print NR' file1
```
- Calculate sum of 2nd column:
```sh
cat file | awk -F " " '{sum+=$2} END{print sum}'
```
- Check if a file exists
```sh
#!/bin/bash

if [ -f file.txt ]; then
	echo "xxx"
else
	echo "xxxx"
fi
```
- Sort number in file:
```sh
sort -n file
```
- Find all files contain xxx
```sh
grep -r "xxx" ./ | cut -d ":" -f 1
```
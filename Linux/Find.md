# Find

## Find
- Find by name, size and user
```sh
find /path -name filename
find /path -name "file*"
find /path -size +20M # > 20M
find /path -size -20M # > 20M
```
- Fast find, need to run update first;
```sh
updatedb # linuc
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.locate.plist # mac
locate filename
```

## Find and Replace text
- grep
```sh
cat file | grep [-ni] "xyz"
grep -r 'rgb2whs' /path # Find content in files
```

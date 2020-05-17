# Task Scheduler

- crond
- Setup: /etc/crontab
```sh
cron
crontab -e
```
- Example 1: cron then edit (every minute run ls)
```sh
# min, hour, date, mon, week
*/1 * * * * ls -l /etc > /tmp/log.txt
```
- E.g. 2 shell, write a shell first
```sh
*/1 * * * * sh xxx.sh
```
- Check scheduled
```sh
crontab -r # stop
crontab -l # list
service cron restart
```
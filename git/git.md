# Summary of Git

## Overview
- Distributed rather than centralized (svn).
- Good resources:
	- https://www.liaoxuefeng.com/wiki/896043488029600
- Concepts:
	- Workspace (your folder);
	- Stage, also index (temporary, added not commited)

## One-time Setup
- Account setup: --global will make all git on your machine use this setup;
```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```
- More setup in file .gitconfig
```
git config --list
git config -e [--global]
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"

git config --global push.default simple
```
- Eable Two-Factor Authorization (Optional)
- Make it work with SSH key, git and remote github is encrypted with ssh;
	- 1. Generate id_rsa and id_rsa.pub in .ssh:
	```
	ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
	# Generating public/private rsa key pair.
	# Enter a file in which to save the key (/home/you/.ssh/id_rsa): [Press enter]
	# Enter passphrase (empty for no passphrase): [Type a passphrase]
	# Enter same passphrase again: [Type passphrase again]
	```
	- 2. Open github, paste the id_rsa.pub in it; one pair for **each** computer;
	```
	eval "$(ssh-agent -s)"
	# Agent pid 59566
	ssh-add ~/.ssh/id_rsa
	# Then in ~/.ssh folder, we have two files (private and public keys)
	```
	- 3. Then always push to git@git... 

## A General process
- 1. Create:
	- Method 1: Create from local and remote add;
	```
	git init [proj] # will add /.git folder
	git remote add origin git@github.com:michaelliao/learngit.git
	```
	- Method 2: create from remote;
	```
	git clone xxx.git
	```
- 2. Develop:
	- Add/remove files into stage;
	```
	git add file1 [file2] [folder] [.]
	git rm ...
	git mv src dst
	```
	- Check in staged codes into master;
	```
	git commit -m [message]
	git commit -a
	git commit -v # show all difference
	git commit --amend [file1] [file2]
	```
	- Check difference
	```
	git status
	git diff
	git log [--pretty=oneline]
	```
- 3. **Version**, go back:
	- About version
	```
	HEAD # current
	HEAD^ # last
	HEAD^^ # last last
	HEAD~100 # last 100 back
	```
	- Go back:
	```
	git reset --hard HEAD^ # reset hard to last
	```
	- Check history commands;
	```
	git reflog # all commits
	git reset --hard xxx_id # could redo
	```
	- **Git manage changes not file**: 1st modify -> git add -> 2nd modify -> git commit, will only commit 1st change; **change not added will not go to commit**;
	- **Throw away** changes in workspace, checkout a file;
	```
	git checkout -- [file.xxx] # reset workspace to staged, -- to avoid branch change
	git reset HEAD [file.xxx] # unstage changes
	```
	- New git uses restore instead of reset and checkout:
	```
	git restore --worktree [file] # same function, from added/staged to workspace
	git restore --staged readme.txt # from master to staged
	git restore --source=HEAD --staged --worktree readme.txt # from master to both staged and workspace
	git restore --staged # same as "git reset HEAD"
	```
- 4. Remote (github)
	```
	git push -u origin master
	```

## Branch
- Basics
	- 1. Create a new branch for develop:
	```
	git checkout -b [branch]
	git switch -c [branch] # same as above line
	```
	- 2. Merge 
	```
	git checkout master
	git switch master # same as above line
	git merge [dev] # merge a specific branch to current
	```
	- 3. Delete after develop
	```
	git branch -d [branch-name] # delete locally
	git push origin --delete [branch-name] # delete remotely
	git branch -dr [remote/branch]
	```
	- Misc:
	```
	git branch # all branches
	git branch -r # all remote branches
	git branch -a # all local and remote
	git branch [name] # create a branch, still stay in current branch
	git checkout [branch]
	git branch --set-upstream [branch] [remote-branch]
	git cherry-pick [commit]
	```
- Conflict
	- 1. Conflict from merge
	```
	git merge branch2
	Auto-merging readme.txt
	CONFLICT (content): Merge conflict in readme.txt
	Automatic merge failed; fix conflicts and then commit the result.
	```
	- 2. git status will show unmerged path;
	- 3. <<<<<<<，=======，>>>>>>> for different branches;
	```
	<<<<<<< HEAD
	Creating a new branch is quick & simple.
	=======
	Creating a new branch is quick AND simple.
	>>>>>>> feature1
	```
	- 4. Make changes and commit;
	- 5. git log will show two lines;
- Develop:
	- When merge, git will use **fast forward** mode; commit of branch info will be gone when deleted;
	- **Disable fast-forward** mode to show branch commits
	```
	git switch -c dev # develop in dev
	git add readme.txt
	git commit -m "add merge"
	git switch master # switch back and merge
	git merge --no-ff -m "merge with no-ff" dev
	git log # will show more commits
	```
	- Suggestions: master seldom changed; everyone checkout own branch from dev and merge to dev;
- **Stash** (for bug fix?)
	- Have unstaged changes (not ready, not supposed to submit), have to change branch to work
	```
	git stash # save changes somewhere
	```
	- Change branch, work on something else;
	```
	git checkout master
	git commit -m "fix bug 101" # 4c805e2
	```
	- Switch back
	```
	git switch dev
	git status # will be clean
	git stash list # show stashed contents
	git stash apply # apply the changes (unstaged changes back!)
	git stash drop # remove stash
	git stash pop # pop = apply + drop
	git stash list # will be empty now
	```
	- Apply the bug fix on current branch
	```
	git cherry-pick 4c805e2 # on dev
	```
- Remote collaboration:
	```
	git remote -v
	git push origin branch-name
	git checkout -b branch-name origin/branch-name
	git branch --set-upstream branch-name origin/branch-name
	git pull
	```
- Rebase: don't want multi-line.
	- Someone pushed, we can do
	```
	git pull
	[... # fix potential conflicts, git add]
	git stats 
	git log # 2 lines
	git rebase # single line
	```

## Tag
- tag on a specific commit
```
git tag v1.0
git tag # will show all, e.g., v0.9, v1.0 ...
```
- Show
```
git show v0.9 # commit id and details
```
- Misc
```
git tag [v1.0] [commit]
git push origin :refs/tags/[tagName]
```

## Misc
- check info
```
git status
git log [--stat]
git log -S [keyword]
git log --follow [file]
git blame [file] # difference between workspace and temporary
git diff HEAD
git diff [branch1] [branch2]
git show [commit]
```
- Remote synchronyze
```
git fetch [remote]
git remote [-v]
git remote show
git remote add [branch]
git pull [remote] [branch]
git push [remote] [branch]
git push [remote] --all
```

## Reset
- Recall a change
```
git checkout [file]
git checkout [commit] [file]
git checkout .
git reset [file]
git reset --soft # work dir only
git reset --hard # both work and temp dir
git reset [commit]
git reset --hard [commit]
git stash
git stash pop
```
- In case of a dirty merge;
```
git reset HEAD --hard
git clean -fd
```

## Everytime Sync with Master
- Option 1: merge;
```
git checkout your_branch
git merge master
```
or
```
git merge your_branch master
```
- Option 2: rebase;
	- Check out master and pull
```
git checkout master
git pull
```
	- Rebase: replay all your modification
```
git checkout your_branch
git rebase master
```
	- Then the branch diverges, you have to use --force to push
```
git push --force
```
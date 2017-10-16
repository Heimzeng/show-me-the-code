# Git learning
	This repository is about git learning of me.
---------------------------------------------
# Start
First of all we should download git in linux with 	
```Bash
$ [sudo] apt-get install git
```
Then we should regist a user to use git with
```Bash
$ git config --global user.name "heim"
$ git config --global user.email "heimzeng@gmail.com"
```
And use
```Bash
$ git config --list
```
to show the config
And we create SSH Key with
```Bash
$ ssh-keygen -t rsa -C "youremail@example.com"
```
get public SSH Key with 
```Bash
$ cd ~/.ssh
$ vi id_rsa.pub
```
to get the public key to place in your github
And now we can clone with this
```Bash
$ git clone git@github.com:Heimzeng/Git-Learning.git
```
Use
```Bash
$ git add -A
$ git commit
```
Add a new branch and push to github
```Bash
$ git checkout -b branchtest
$ git remote add branchtest git@github.com:Heimzeng/Git-Learning.git
```
Switch to master branch
```Bash
$ git checkout master
```
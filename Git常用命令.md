查看本地分支： git branch

查看远程分支： git branch -r

查看所属分支： git branch -a

切换分支： git checkout <分支名>

创建分支：git branch <分支名>

创建并切换分支：git checkout -b <分支名>

代码提交：git commit

代码提交加描述：git commit -a -m 'commit new code'

合并分支：git merge <要合并的分支>

拉取某次提交： git cherry-pick <日志号>

删除远端分支：git push origin --delete <分支名>

删除分支指针（本地分支）：git branch -d  <分支名>【只删除指向该commit号的指针，并不会删除其相关的提交号, 在日志中仍然可以找到之前的commit记录，也仍然可以在该commit上创建新的分支】

下载远程的库的内容，不做合并：git fetch 

放弃本地修改强制更新：git reset origin/develop --hard

回退命令：git reset --hard HEAD^

回退到n次提交之前：git reset --hard commit_id

查看提交记录：git log；

强推到远程：git push origin HEAD --force

 

删除远程仓库文件：（1） git rm --cached "文件路径"，不删除物理文件，仅将该文件从缓存中删除；（2） git rm --f "文件路径"，不仅将该文件从缓存中删除，还会将物理文件删除（不会回收到垃圾桶）。

 

假如有文件不小心commit到了服务器想删除它:

git rm -- cached "路径+文件名" ；

git commit -m "delete file" ；

git push；

git rm -r "路径+文件名" ；

git commit -m "delete file"；git push

 

 

假如想回退代码：

1.git log 查看想要回退到哪个commit版本，复制版本号

2.git reset --hard commit_id 

3.git push origin xxx if 强制push到远程分支

1. 克隆github
git clone https://github.com/wangsongf/linux.git
2. 配置文件
vim .git/config
url = https://wangsongf@github.com/wangsongf/python.git
3. 新增文件
git add *
git commit -m 'test add'
 git push
4.删除文件
git rm test.txt
git commit -m 'test rm'
 git push
5.移动文件
git mv test.txt test/
git commit -m 'test mv'
git push
6.查看帮助和日志
git --help
git log
7.拉取远程文件
git pull

提示异常：
(gnome-ssh-askpass:16845): Gtk-WARNING **: cannot open display: 

解决方法：
unset SSH_ASKPASS

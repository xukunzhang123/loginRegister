"""
git init
git log
git add *
git commit -m " add init  usl/views"
git status

(loginRegister) PS C:\Users\ZXK\PycharmProjects\day_08\loginRegister> git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   login/urls.py
        new file:   templates/login/index.html
        new file:   templates/login/login.html
        modified:   "doc/01_\346\255\245\351\252\244\350\256\260\345\275\225.py"
        modified:   login/urls.py
        modified:   login/views.py
        modified:   loginRegister/urls.py
        modified:   templates/login/index.html
        modified:   templates/login/login.html

git diff login/views.py     #查看变化


# git提交代码到本地仓库
ssword:安装git,在 Terminal 中报错时，要设置他的环境变量。
1. 初始化git:  git init
Initialized empty Git repository in C:/Users/ZXK/PycharmProjects/day_08/loginRegister/.git/

2. 安装插件 .ignore ，并生成python上传文件需要忽略的内容

在File中的setting中设置 下载 ignore插件，安装之后，在新建时会有一个.ignore的扩展，
选择 .ignorefile  选择PYTHON之后便会有一个新文件。

3. 添加修改到暂存区
git add *   #将代码提交到暂存区
warning: in the working copy of '.idea/inspectionProfiles/Project_Default.xml', LF will be replaced by CRLF
the next time Git touches it
warning: in the working copy of '.idea/inspectionProfiles/profiles_settings.xml', LF will be replaced by CRL
F the next time Git touches it

4. 将暂存区的代码提交到本地git仓库
 git commit -m "创建项目环境" #提交代码到仓库

5. 查看历史提交记录
git log
Password (again):


新建分支：
git branch name     # 新建分支
git branch          # 查看分支
pycharm             # 右下角可以切换分支、新建分支等
git log             # 查看提交历史
git reset --hard    # 返回到某一个的状态

将本地仓库和远程仓库关联起来。
git remote add origin https://github.com/xukunzhang123/loginRegister.git

"""


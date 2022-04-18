"""
git 简介
    1.什么是git
        git是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件
    2.代码管理工具的用途
        1.防止代码丢失，做备份
        2.项目的版本管理和控制，可以通过设置节点进行跳转
        3.建立各自的开发环境分支，互不影响，方便合并
        4.在多终端开发时，方便代码的相互传输
    3.git的特点：
        1.git是开源的，多在*int下使用，可以管理各种文件
        2.git是分布式的项目管理工具（svn是集中式的）
        3.git数据管理更多样化，分享速度快，数据安全
        4.git拥有更好的分支支持，方便多人协调
    4. git安装
        sudo apt-get install git
git 使用
    基本概念：
        工作区：项目所在操作目录，实际操作项目的区域
        暂存区：用于记录工作区的工作（修改）内容
        仓库区：用于备份工作区的内容
        远程仓库：远程主机上的git仓库
        **注：在本地仓库中，git总是希望工作区的内容与仓库区保持一致，而且只有仓库去的内容才能和其他远程仓库交互
    初始配置
        配置命令： git config
            配置所有用户： git config --system【选项】
                配置文件位置：/etc/gitconfig
            配置当前用户：git config --global【选项】
                配置文件位置：~/.gitconfig
            配置当前项目：git config【选项】
    配置git操作：
        1.配置用户名
            eg
                将用户名设置为：Lime: runas(linux系统用sudo) git config --system user.name Lime
                    查看配置文件：cat /etc/gitconfig

        2.配置用户邮箱
            eg
                将邮箱设置为569430899@qq.com: git config --global user.email 569430899@qq.com

        3.配置编译器
            eg
                配置编译器为pycharm： git config core.editor pycharm

        4.查看配置信息：
            git config --list

        5.将文件同步到本地仓库
            git commit [file] -m[message]
                说明：-m表示添加一些同步信息，表达同步内容
                    eg
                        git commit -m 'add files'
                        git commit -m 'init add'（commit后面没有指定文件，则是将所有暂存区的文件全部提交至仓库区）

        6.查看commit日志记录
            git log
            git log --pretty=oneline

        7.比较工作区文件和仓库区文件差异
            git diff 【file】

        8.将暂存区或者某个commit点文件恢复到工作区
            git checkout [commit] -- [file]
             eg
                git checkout -- README.md
                rm girl.jpeg(移除某个文件)
                git checkout -- girl.jpeg
            * -- 是为了防止误操作，checkout还有切换分支的作用

        9.移动或删除文件
            git mv 【file】 【path】
            git rm 【files】
                *注意：这两个操作会修改工作区内容，同时将操作记录提交到暂存区

        10.创建项目
            1.mkdir gitproject
                切换至该目录： cd gitproject/
                查看该目录下内容： ls
            2.git init(初始化仓库)
                    意义： 将某个项目目录变为git操作目录，生产git本地仓库。即该项目目录可以使用git管理
            3.配置编译器
                git config core.editor pycharm
            4.ls -a 查看隐藏文件
            5.cat .git/config 查看该项目配置文件
            6.git config --list 查看所有配置信息
            配置文件位置： project/.git/config
    基本命令：
        1.初始化仓库：
            git init
                意义： 将某个项目目录变为git操作目录，生产git本地仓库。即该项目目录可以使用git管理
        2.查看本地仓库状态
            git status
                说明：初始化仓库后默认工作在master分支，当工作区与仓库去不一致时会有提示。
        3. 将工作内容记录到暂存区
            git add
                git add dict.txt: 提交单一文件到暂存区
                git add girl.jpeg mysql.py ： 提交多个文件到暂存区（以空格隔开）
                git add test/： 提交一个文件夹（包含里面的每一个文件）
                git add.(当前目录下所有内容)
                git add*（所有文件  但是不能提交隐藏文件）
                需要提交隐藏文件时直接指定该文件：git add .idea/
                或者使用、@扩展规则内容：
                    @扩展规则：
                        在git项目中可以通过在项目的某个文件夹下定义.gitignore文件的方式，规定相应的忽略规则，用来管理当前文件夹下的文件的git提交行为。
                        .gitignore文件是可以提交到公有仓库中，这就为该项目下的所有开发者都共享一套定义好的忽略规则。在.gitignore文件中，遵循响应的语法，
                        在每一行指定一个忽略规则。
                            .gitignore忽略规则简单说明：
                            file        表示忽略file文件
                            *。a         表示忽略所有.a结尾的文件
                            ！lib.a      表示但lib.a除外
                            build/      表示忽略build/目录下的所有文件，过滤整个build文件夹。

        4. 取消文件暂存记录
            git rm --cached[file](撤销将文件提交至暂存区)
                git rm --cached README.md()

        5.将文件同步到本地仓库
            git commit [file] -m[message]
                说明：-m表示添加一些同步信息，表达同步内容
            git commit -m 'init add'（没有指定file，表示将所有暂存区文件全部提交至本地仓库）
                住：没有记录到暂存区的内容是不会被提交到本地仓库的

        6.查看commit日志记录
            git log
            git log --pretty=oneline

        7.比较工作区文件和仓库区文件差异
            git diff test.md

        8.将暂存区或者某个commit点文件恢复到工作区
             git checkout [commit] -- [file]
                ** -- 为了防止误操作，checkout还有切换分支的作用，
             git checkout -- test.md（）
                 rm girl.jpeg（将文件删除）
                 ls(查看当前目录下不再包含文件girl.jpeg)
                 git checkout -- girl.jpeg(将文件从本地仓库恢复至当前目录下)
                 ls（查看当前目录，文件girl.jpeg恢复）

        9.移动或删除文件
            git mv 【file】 【path】
                git mv dict.txt test/（将文件dict.txt移动至文件夹test下）
            git rm 【files】
                *注意：这两个操作会修改工作区内容，同时将操作记录提交到暂存区

    版本控制（依赖于仓库区的备份内容）
        1.退回到上一个commit节点
            git reset --hard HEAD^（HEAD表示当前最新的状态的一个指针）
                注意：一个^表示回退一个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致
                操作实质：先将仓库区退回到上一个版本，再让工作区与仓库区同步

        2.退回到指定的commit_id节点
            git reset --hard [commit_id]

        3.查看所有操作记录
            git reflog
                注意：最上面的是最新的记录，可以利用commit_id去往任何操作位置

        4.创建标签
            标签：在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代
                git tag[tag_name] [commit_id] -m [message]
                    说明：commit_id可以不写则默认标签表示最新的commit_id位置，[message]也可以不写，但是最好添加
                eg
                    在最新的commit处添加标签v1.0
                        git tag v1.0 -m '版本1'
                        git tag v0.5 1c733ee（在指定commit_id处） -m '版本0.5'

        5.查看标签
            git tag

        6.去往某个标签节点
            git reset --hard v0.5（不同版本之间跳转）

        7.删除标签
            git tag -d v0.5(当某个标签失去作用时可以删除)

    保存（封存）工作区
            操作前工作区状态
                git status
                    $ git status
                    On branch master
                    nothing to commit, working tree clean

        1.保存工作区内容（保存前保证暂存区没有内容需要提交，即工作区、仓库区同步）
            git stash save [message]
                说明：将工作区未提交的修改封存，让工作区回到修改之前的状态
                    eg  git stash save '修改第一个二级标题'（方案1）
                        git stash save '修改第二个二级标题'（方案2）
                        git stash save '修改第一个三级标题'（方案3）
                        注释：（则对每一种方案进行封存，对外不可见，工作区回到修改之前的状态）
                            三种方案，相当于保存了3个工作区内容

        2.查看工作区列表-
            git stash list
                stash@{0}: On master: 修改第一个三级标题
                stash@{1}: On master: 修改第二个二级标题
                stash@{2}: On master: 修改第一个二级标题
                说明：最新保存的工作区在最上面

        3.应用某个工作区
            git stash apply [stah@{n}]
                、经过最终研判，认定方案2比较合理，因此应用方案2
                    git stash apply stash@{1}（应用至方案2的状态）
                        并将最终方案add至暂存区，commit至仓库区
                             git add test.md
                             git commit  -m '选定方案2'
        4.删除某个工作区
            在选定最终方案后，其余方案可以删除；
                 git stash drop stash@{0}
                    删除最新的修改（stash@{0}）后，其他的修改会往前补
                git stash clear: 清除工作区全部内容

    分支管理：
        定义： 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，单独开发，互不干扰。完成开发工作中后再进行分支同意合并。
        意义：在其中一个分支a操作数据、内容兵团提交至仓库去后，切换至另一分支b后，会恢复至分支未进行任何操作的状态，这也就为多人同时完成同一个项目有了很好的办法。

        1.查看分支情况
            git branch
                说明：前面带*的分支表示当前工作分支

        2.创建分支
            git branch [branch name]
                说明：基于a分支创建b分支，此时b分支会拥有a分支的全部内容，在创建b分支时最好保持a分支的干净状态。
                    在那个分支建立新的分支就是基于哪个分支建立的分支

        3.切换分支
            git checkout excel（区分于将暂存区或者某个commit点文件恢复到工作区：git checkout [commit] -- [file]）

            ****
                git checkout -b microsoft 同时具备2和3的功能：即新建一个分支并切换至该分支。

        4.将新建分支合并回到主分支master
            将分支a修改完成后，切换至主分支master，再执行命令
                git merge 分支a【name】
            合并后会发现，在分支a里面做的修改已全部出现在主分支master中。
        ****冲突情况说明：
            主分支master下建立新的分支a、b
            a、b同时都做出了修改
            a、b修改后切换回master正常执行merge a大的命令
            在执行merge b时由于master已经发生改变（已经将a合并），所以会产生冲突
            解决办法：
                按体统提示进行完善操作并commit即可。
        ****冲突情况说明：
            主分支master下建立新的分支a、b
            a、b在同一位置、指针（HEAD）处做了修改
            在执行merge 第二分支时就会产生冲突
            解决办法：
                按体统提示将文件修改或删除或整合并commit即可。

        5.删除分支
            git branch -d [branch]  #删除分支
            git branch -D [branch]  #删除没有被合并的分支

    远程仓库
        远程主机上的git仓库。实际上git是分布式结构，每台主机的git仓库结构类似，知识把别人主机上的git仓库称为远程仓库。

        GitHub介绍
            github是一个开源的项目社区网站，拥有全球最多的开源项目。开发者可以注册网站在github建立自己的项目仓库。

        网址： github.com

        代码管理工具： git

            获取项目：
                在左上角搜索栏搜索想要获取的项目
                选择项目后复制项目的git地址（clone or download）
                在本地使用git clone方法即可获取
                    git clone https://github.com/TheAlgorithms/Python.git(获取到的项目git地址)
            ****注意： 获取到本地的项目 会自动和github远程仓库建立连接。且获取的项目本身也是个git项目

        创建git仓库
            点击右上角加号下拉菜单，选择新的仓库
            填写相应的项目信息即可
            github仓库相对本地主机就是一个远程仓库 通过remote连接，如果需要输入密码，输入github密码即可。连接后即可使用远程仓库命令操作。readme文件会被自动作为项目介绍
            如果是在即的仓库在仓库界面选择setting，在最后可以选择删除仓库


        远程仓库操作命令：
            所有操作在本地git仓库下执行
                1.添加远程仓库：
                    git remote add origin https://github.com/bo0oby/AID-1906.git

                2.删除远程主机
                    git remote rm [origin]

                3.查看连接的主机
                    git remote
                        ***注意：一个git项目连接的主机名不会重复

                4.将本地分支推送给远程仓库
                    git push（上传） -u（第一次上传某个分支时使用） origin master（将master（分支）上传到远程主机（origin）的git仓库）
                    ****第一次-u会对分支进行关联，以后每次更新只需要用git push 命令同步即可

                    标签上传：


































"""





















































































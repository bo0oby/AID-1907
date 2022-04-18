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
                配置文件位置： project/.git/config
    基本命令：
        1.初始化仓库：
            git init
                意义： 将某个项目目录变为git操作目录，生产git本地仓库。即该项目目录可以使用git管理
        2.查看本地仓库状态
            git status
                说明：初始化仓库后默认工作在master分支，当工作区与仓库去不一致时会有提示。
        3.将工作内容记录到暂存区：
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

            @扩展规则：
                在git项目中可以通过在项目的某个文件夹下定义.gitignore文件的方式，规定相应的忽略规则，用来管理当前文件夹下的文件的git提交行为。
                .gitignore文件是可以提交到公有仓库中，这就为该项目下的所有开发者都共享一套定义好的忽略规则。在.gitignore文件中，遵循响应的语法，
                在每一行指定一个忽略规则。
                    .gitignore忽略规则简单说明：
                    file        表示忽略file文件
                    *。a         表示忽略所有.a结尾的文件
                    ！lib.a      表示但lib.a除外
                    build/      表示忽略build/目录下的所有文件，过滤整个build文件夹。


"""





















































































# NukeToolSet
### Nuke工具集说明
大部分都是这几年干合成用到的，有些自己写的，有些朋友写的，有些网上down的！现在免费开源共享，希望大家都来共享自己的nuke插件！

### NukeToolSet安装
在.nuke文件夹下面创建一个init.py

``` stylus
nuke.pluginAddPath("插件路径")
cgspread_root_path = ("插件路径")
```
示例

``` stylus
nuke.pluginAddPath("E:/Nuke_plugin/nuke_plugin/")
cgspread_root_path = "E:/Nuke_plugin/nuke_plugin/"
```

### 加入开发

 1. fork 这个项目到自己的github
 2. 修改 提交pull request 给我
 3. 我审核后合并主分支

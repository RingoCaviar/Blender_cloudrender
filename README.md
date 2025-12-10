# BLENDER_CLOUDRENDER

## 使用方法

1. 用一个**英文的文件夹**装好你的工程和所有素材
2. 把Blender_render_scripts文件夹中的所有脚本都复制到你创建的**英文文件夹中**
3. 然后上传**英文文件夹**到AutoDL服务器中
4. 在服务器的**Jupyter Notebook**控制面板中，打开“一键部署Blender.ipynb”文件
5. 根据提示操作

## 更新

### v3.0

🟢删除了通过镜像部署的方法，现在只推荐把脚本和BL工程复制到一个文件夹里然后上传服务器的方法使用。

🟢该脚本主要通过Jupyter Notebook便捷实现，所以要确保你的服务器支持。

🟢推荐把东西都打包到一个文件夹中，你上传的文件夹应该是这个结构👇

```
📦Blender_render_scripts(可以改名)
 ┣ 📜bl_py.py
 ┣ 📜setting.py
 ┣ 📜install_blender.py
 ┣ 📜你的工程.blend(可以改名)
 ┗ 📜一键部署Blender.ipynb
```

🟢setting.py脚本的作用：将Blender设置为显卡渲染。因为服务器刚下载的Blender默认是CPU渲染，必须用脚本改一下首选项的设置，否则合成器还是用CPU，降噪也是CPU，速度极慢。  

## 作用

🟢在AutoDL等服务器上快捷部署Blender进行渲染

## 什么人需要它？

🔹当你需要使用Blender渲染一帧超高质量的图片，渲染时间大概要几个小时甚至十几个小时。

🔹当你需要渲染一段动画，本地渲染速度无法满足需求并且其他渲染平台价格较高时。

## AutoDL服务器创建指南：

1. 推荐选择西北地区或者重庆地区的4090D 24G，数据盘50G一般够用，不够可以扩容。价格一般是2块钱一小时，按量计费。
3. 使用镜像创建的服务器无需进行环境配置，直接运行渲染指令即可，运行前一定要更改渲染命令，关于渲染命令的含义可以查询Blender官方手册的[命令行渲染部分](https://docs.blender.org/manual/zh-hans/4.2/advanced/command_line/arguments.html#command-line-arguments)。

###### ❗❗❗此脚本仅有<u><font color=#FFC0CB>辅助作用</font></u>，linux基础命令需要掌握一些，比如cd命令。blender命令行渲染的相关参数在[官方手册](https://docs.blender.org/manual/zh-hans/4.2/advanced/command_line/arguments.html#command-line-arguments)中查询。

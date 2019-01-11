---
title: Anaconda3详细安装教程
date: 2018-12-10 13:19:01
tags:
---

## 1. 官网下载Anaconda3
```
https://anaconda.com/download/
```
## 2. 测试是否安装正确
```
在cmd中输入conda info
如果显示不是内部内容则在环境变量中配置环境
```
## 3. 环境配置
我是下载在d盘ProgramData目录下
```
D:\ProgramData\Anaconda3;
D:\ProgramData\Anaconda3\Scripts;
D:\ProgramData\Anaconda3\Library\mingw-w64\bin;
D:\ProgramData\Anaconda3\Library\usr\bin;
D:\ProgramData\Anaconda3\Library\bin;
```
## 4. 设置Anaconda镜像
使用conda install 包名 安装python非常方便，但是官网在国外下载速度慢，这里用清华大学提供的仓库镜像
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/c
conda config --set show_channel_urls yes
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/`
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```
## 3. 管理包
```
1. 安装包
conda install matplotlib 或者 pip install matplotlib

2. 卸载包
conda remove matplotlib

3. 跟新包
conda update matplotlib

4. 查询已经安装的包
conda list
```
## 环境管理

conda可以提供不同的项目建立不同的运行环境
### 1.创建python3.6环境
```
conda create -n python27 python=2.7
```
### 2. 进入环境
```
conda activate python36
```
### 3. 离开环境
```
deactivate
```
### 4. 删除环境
```
conda env remove -n python36
```













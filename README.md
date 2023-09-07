# python

## 虚拟环境

### conda

conda 将几乎所有的工具、第三方包都当作 package 进行管理，甚至包括 python 和 conda 自身。Anaconda 是一个打包的集合，里面预装好了 conda、某个版本的 python、各种 packages 等。

```bash
conda -V
# 更新当前conda
conda update conda

# 查看当前存在哪些虚拟环境
conda env list
conda info -e

# 查看环境中安装了哪些包,默认是base环境
conda list

# 创建虚拟环境

conda create -n [env_name] python=x.x
# 或者克隆
conda create -n [env_name] --clone env_name

# 激活虚拟环境
source activate [env_name]
conda activate [env_name]

# 安装额外包
conda install [package]

# 关闭虚拟环境
source deactivate
conda deactivate

# 删除虚拟环境
conda remove -n [env_name] --all

# 删除虚拟环境中的某个包
conda remove --name $env_name $package_name

# conda 设置国内镜像, 清华
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

# 恢复默认镜像
conda config --remove-key channels

# 安装某些包
conda install -c anaconda scikit-learn    # 安装sklearn
pip install -i pypi.douban.com/simple tensorflow-gpu==1.14   #用豆瓣源安装包，上面的清华园同理，记得-i
```

## 如何一键安装所有第三方库文件？

[https://github.com/jayboxyz/deeplearning-cv-notes/blob/master/01_python/python_basic/Python%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E6%89%80%E6%9C%89%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93.md](https://github.com/jayboxyz/deeplearning-cv-notes/blob/master/01_python/python_basic/Python%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E6%89%80%E6%9C%89%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93.md)

## pip freeze

在查看别人的 Python 项目时，经常会看到一个 `requirements.txt` 文件，里面记录了当前程序的所有依赖包及其精确版本号。这个文件有点类似与 Rails 的 Gemfile。其作用是用来在另一台 PC 上重新构建项目所需要的运行环境依赖。

`requirements.txt` 用来记录项目所有的依赖包和版本号，只需要一个简单的 pip 命令就能完成。

进入到需要导出所有 Python 库的那个环境，然后使用那个环境下的 pip ：

```python
pip freeze > requirements.txt
```

> requirement.txt 文件默认输出在桌面。
>
> 注：查看源文件，pip 的 freeze 命令用于生成将当前项目的 pip 类库列表生成 requirements.txt 文件。

然后就可以用：

```python
pip install -r requirements.txt
```

来一次性安装 `requirements.txt` 里面所有的依赖包，真是非常方便。

`requirements.txt` 文件类似如下：

```python
Django=1.3.1
South>=0.7
django-debug-toolbar
```

将模块放在一个列表中，每一行只有一项。

---

## pipreqs

### pipreqs 的作用

> 一起开发项目的时候总是要搭建环境和部署环境的，这个时候必须得有个 python 第三方包的 list，一般都叫做 requirements.txt。 如果一个项目使用时 virtualenv 环境，还好办 `pip freeze` 就可以解决，但是如果一个项目的依赖 list 没有维护，而且又是环境混用，那就不好整理的呀，不过，这里安利一个工具 pipreqs，可以自动根据源码生成 `requirements.txt`。

pip freeze 命令：

```python
pip freeze > requirements.txt
```

这种方式配合 virtualenv 才好使，否则把整个环境中的包都列出来了。

### pipreqs 的使用

pipreqs 这个工具的好处是可以通过对项目目录的扫描，自动发现使用了那些类库，自动生成依赖清单。缺点是可能会有些偏差，需要检查并自己调整下。

pipreqs 的安装：`pip install pipreqs`

使用方式也比较简单，直接进入项目下然后使用 `pipreqs ./` 命令即可，如：

```
pipreqs ./
```

如果是 Windows 系统，会报编码错误 (UnicodeDecodeError: 'gbk' codec can't decode byte 0xa8 in position 24: illegal multibyte sequence) 。这是由于编码问题所导致的，加上 encoding 参数即可，如下：

```python
pipreqs ./ --encoding=utf-8
```

生成 `requirements.txt` 文件后，可以根据这个文件下载所有的依赖。

```python
pip install -r requriements.txt
```

附：

```xml
详细用法：
pipreqs [options] <path>

选项：
    --use-local仅使用本地包信息而不是查询PyPI
    --pypi-server <url>使用自定义PyPi服务器
    --proxy <url>使用Proxy，参数将传递给请求库。你也可以设置

    终端中的环境参数：
    $ export HTTP_PROXY =“http://10.10.1.10:3128”
    $ export HTTPS_PROXY =“https://10.10.1.10:1080”
    --debug打印调试信息
    --ignore <dirs> ...忽略额外的目录
    --encoding <charset>使用编码参数打开文件
    --savepath <file>保存给定文件中的需求列表
    --print输出标准输出中的需求列表
    --force覆盖现有的requirements.txt
    --diff <file>将requirements.txt中的模块与项目导入进行比较。
    --clean <file>通过删除未在项目中导入的模块来清理requirements.txt。
```

## 参考文章：

-   [python 批量导出项目所依赖的所有库文件及安装的方法（包导出与导入）](https://blog.csdn.net/mezheng/article/details/84317515)
-   [Python 使用 requirements.txt 安装类库](https://www.cnblogs.com/zknublx/p/5953921.html)
-   [浅谈 pipreqs 组件(自动生成需要导入的模块信息)](https://www.cnblogs.com/fu-yong/p/9213723.html)

## python 基础

**python**的项目有时候一些基础知识不牢固,导致出了很多问题.所以需要多加强一下基础知识.

```python
# int(python也没有short,long之分)
# float(python没有单双精度之分,因为python里面默认是双精度一种类型)
type(1)
type(1.1)
type(1.1111111111111)
type(1+0.1)
type(1+1.0) # float

# TODO: 牢记下面这个知识点 // 表示整除
type(2/2) # float
type(2//2) # int
type(1//2) # int

# 2进制
0b10
# 8进制
0o10
# 16进制
0x1F
# 其他进制转换2进制
bin(10), bin(0o7), bin(0xE)
# 其他进制转换8进制
oct(0b111),oct(0x777)
# 其他进制转换10进制
int(0b11), int(0o77)
# 其他进制转换16进制
hex(888), hex(0o7777)

# 布尔类型
True, False
bool(0) # 表示False 非0表示True
# 复数 complex

# 字符串, 单引号,双引号,三引号(可以是三个单引号或者三个双引号)
# 单引号和双引号表示的意思是一样的.
a = "let's go" # 这样就很方便了
a = '''
hello 回车了
end.
'''
# r原始字符串 raw str
print(r'c:\northwind\northwest')

# list 列表 非常灵活
type([1,2,3,4,5,6])
type(["hello", 1, 9, True, False, "world"])
type([[1,2],[3,4],[True, False]])

# tuple 元组
(1,2,3,4)
type((1)) # int
type((1,)) # tuple

# str, list, tuple序列 共有的操作
3 in [1,2,3,4,5] # True
3 not in [1,2,3,4,5] # False
len((1,2,3,4,5)) # 5
max([1,2,3,4,5,6]) # 6
min([1,2,3,4,5,6]) # 1

# 集合: set dict
# 集合最大的特点是无序的, 无序的话就不能用下标或者切片操作来找值
# 集合是不重复的
# set
type({1,2,3,4,5,6}) # set 类型
len({1,2,3})
1 in {1,2,3}
1 not in {1,2,3}
type(set()) # 定义空set
type({}) # 定义空的dict

# dict
{1:"hello", "1": "world", (1,2,3):"ok"}

# 值类型和引用类型
# 值类型: 字符串,元组,数值 本身不允许被修改
# 引用类型: 列表,集合,字典 本身允许修改

```

包 >> 模块 >> 类 >> 函数,变量

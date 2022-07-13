# Readme

本项目为作业提交，使用pygtrans lib，因此无法使用googletrans库的人可以试试我这一版。

同样的，用户只需将自己的生词全部写进`./collection.txt`文件，这个项目甚至支持单词之间参杂有奇怪的分隔符...

参数：

```python
1. -n 表示用户希望复习的单词数
2. -s 表示用户希望从第几个单词开始
3. -l 表示用户希望复习的单词范围大小
```

例如：`python3 generator.py -n 100 -s 20 -l 200` 表示希望从生词本的第 20 个单词开始到第 220 个单词结束的范围内随机抽取 100 个生词生成生词本。(本项目只支持随机抽取，因为令n=l即可实现顺序抽取...)

生词本存放于 `./data` 路径下，含有翻译完全和未翻译两种。旧的生词本不会被新生成的生词本覆盖。

# 项目环境

python版本3.8，项目主要依赖于包pygtrans，安装指令：

```shell
pip install pygtrans
```

其他库可查看`generator.py`源码自行配置。

需要注意的是，由于pygtrans依赖translate.google.com，因此中国大陆用户需自行配置网络环境（科学上网），对于wsl2用户，需要提醒的是wsl并不走windows主机的代理，所以需要自己设置代理。方法如下（良心）：

1.查看wsl的dns服务器地址（即Windows主机在wsl网络中的地址）：

```shell
cat /etc/resolv.conf
```

2.找到以后添加代理：

```shell
export ALL_PROXY="http://$(your_ip_here):$(port_here)"
# 例如我通过上一步看到ip是172.21.64.1，代理用的端口是7890（clash用户默认的端口就是7890），我就输入：
# export ALL_PROXY="http://172.21.64.1:7890"
```

以上两步可以统一写成一个`.proxyrc`（如果你设置端口为7890）：

```shell
#! /bin/bash

host_ip=$(cat /etc/resolv.conf | grep "nameserver" | cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
```

然后每次运行`source .proxyrc`就能让当前终端翻墙了。

可以运行：

```shell
curl www.google.com
```

看看是否可以翻墙。
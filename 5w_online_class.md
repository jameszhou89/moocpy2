# 5W online class

## list
在这个小结里面，强调了list的用法，同时也记录了一个功能诞生的过程：求100以内的素数。

求素数的核心方法：把某个数字除以小于其的所有数字，并求余。如果余数有0，则不是素数。

* [d for d in range(2,x-1)]    #列出x以内的数字#
* [x%d for d in range(2,x-1)] #对x求x以内的数字的余数#
* 0 not in [x%d for d in range(2,x-1)] #判断哪些数的余数不是0#
* [p for p in range(2,x-1) if 0 not in [p%d for d in range(2,p-1)] ]

## 加密

通过结合两个内置的库 hashlib 和 Base64

1）from hashlib import md5

hashlib是个专门提供hash算法的库，现在里面包括md5, sha1, sha224, sha256, sha384, sha512，使用非常简单、方便。 
md5经常用来做用户密码的存储。而sha1则经常用作数字签名。
md5是单向的字符串指纹。


[hashlib介绍文档](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868328251266d86585fc9514536a638f06b41908d44000)

[官方文档](https://docs.python.org/2/library/hashlib.html)

[中文文档](http://blog.csdn.net/tys1986blueboy/article/details/7229199)

2) from base64 import urlsafe_b64encode, urlsafe_b64decode

Base64是一种用64个字符来表示任意二进制数据的方法。

用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。

Base64是可逆操作的编码。

[base64--廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001399413803339f4bbda5c01fc479cbea98b1387390748000)

[Base64 编码原理简介和python的base64模块的使用](http://blog.csdn.net/magictong/article/details/2687183)




## 俄罗斯的数学和计算机能力

听大妈聊到俄罗斯强大的数学能力，搜了几篇文章

1.[世界第一数学强校的背后](http://blog.csdn.net/xianlingmao/article/details/5528030)

2.[俄罗斯黑客在国际黑客圈中地位如何？](http://www.zhihu.com/question/24765834)



## 团队协作

8w~10w,每周迭代一个版本，组队小于4个人。










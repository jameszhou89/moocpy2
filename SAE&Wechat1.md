# 接入微信公众号

1.在SAE上创建Python应用

![](cdata1.png)

2.在SAE上部署代码
根据这篇文章的提示，进行代码部署

[代码部署手册](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html#svn?ticket=00052aff700e7a05bffcbc867d340f2754363ca7)

部署成功，上图
![](deploy1.png)


3.申请消息接口并验证

1)消息接口配置

填写urL 
    
    2.cdata1.sinaapp.com 

其中2是指第二个版本。并填写token


2)消息接口验证（网址接入）

在这个过程中由于忘记填写 request
    
    "from bottle import Bottle, run, route, request"
导致服务器不能正确配置，微信平台服务器配置无法正常启用。






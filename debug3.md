# debug3

有一些气馁，花了两个晚上debug都没有成功。分析原因，主要是没有去一个个排除可能的bug，而是去猜测。所以，接下来会排除一个一个的潜在bug.

1.金数据返回的数据格式不对

有可能金数据返回的数据，用request.body.read()读取后，用json.load不能解析成python格式。

所以我直接把content改成一个具体的数据，但是在微信公众后台上依然未能返回数据。说明，这个问题跟金数据的读取无关。

2.测试微信能否接受到普通的信息输入

http://mp.weixin.qq.com/wiki/17/fc9a27730e07b9126144d9c96eaf51f9.html

出现问题了

微信公众平台接口调试工具

![](request fault.png)

SAE日志中心

![](sae log.png)
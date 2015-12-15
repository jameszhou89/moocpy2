# 微信消息推送和回复


## 逻辑设计

### 微信公众号端
1. 微信服务器接受到用户发出的消息，格式为xml
2. SAE服务器解析xml格式文件，得到数据msg

### 金数据端
1. 用户提交表单之后，表单向服务器的url以JSON格式POST该数据。
2. SAE服务器读取金数据的数据data（并向金数据返回指令？）
3. 将数据data转换为xml格式的数据data。

### 微信和金数据的交互

1. SAE服务器对数据msg进行判断，如果msg为约定的数据，则SAE向微信公众号端发送xml格式的数据data,如果不是则返回None.


## divide&conquer

懂得流程之后后，书写伪代码。

    # coding:utf-8
    #! /usr/bin/env python
    from bottle import Bottle, run, route, request, BaseRequest, get, post
    import xml.etree.ElementTree as ET

    import json
    import sae
    import sys
    import hashlib
    import time

    app = Bottle()

    @app.route('/',method="POST")
    def getdata_from_jishuju():
    """从金数据返回的数据中提取jason格式的信息
    """
        #origin_data=BaseRequest.json()
        origin_data=request.params()

        #将json格式转化为python结构
        data = json.loads(origin_data)
        return data

    @app.route('/weixin')

    def check_signature():
        token ='cdata1'
        timestamp = request.GET.get('timestamp', None) 
        nonce = request.GET.get('nonce', None) 
        signature = request.GET.get('signature', None)  
        echostr = request.GET.get('echostr', None) 

        L = [token,timestamp,nonce]
        L.sort()
        s=L[0]+L[1]+L[2] 

        if hashlib.sha1(s).hexdigest()  == signature:
            return echostr
        else:
            return None

    def parse_msg(rawmsgstr):
    """这里用来解析微信Server Post过来的XML数据的
    取出各字段对应的值，以备后面的代码调用，也可用lxml等模块。
    """
        #import xml.etree.ElementTree as ET
        root = ET.fromstring(rawmsgstr)
        msg = {}
        for child in root:
            msg[child.tag] = child.text
        return msg


    def response_msg(recvmsg, content):
    """将金数据的内容从jason格式转化为xml,并发送给微信公众平台
       recvmsg是指从金数据拿到的数据
       content是指金数据的内容
    """
    recvmsg = request.body.read() 
    content = getdata_from_jishuju()

    textTpl = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[%s]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        <FuncFlag>0</FuncFlag>
        </xml>"""
    echostr = textTpl % (recvmsg['FromUserName'], recvmsg['ToUserName'], recvmsg['CreateTime'], recvmsg['MsgType'], content)
    return echostr


    @app.route("/weixin",method="POST")
    def response_weixin():
    """
    这里是响应微信Server的请求，并返回数据的主函数，判断Content内容
    如果是跟预设的值("1")一样，就调用纯文本格式返回
    recvmsg是指从微信公众号拿到的数据
    """

     #拿到并解析数据
        recvmsg = request.body.read() 
        msg = parse_msg(recvmsg)

        if msg["Content"] == "1":
            return response_msg(recvmsg, content)
        else:
            return None


    application = sae.create_wsgi_app(app)

    if __name__ == "__main__":
        app.run(debug=True)

    #from bae.core.wsgi import WSGIApplication
    #application = WSGIApplication(app)























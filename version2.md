# version2

感谢教练在C2T2上的耐心指导，目前已经成功打通了金数据/SAE/微信之间的互动。

贴出代码，然后分析一下


## 1. 第二个版本核心代码

    @app.route('/',method="POST")
    def response_jishuju():
        print "getdata_from_jinshuju"
        origin_data=request.body.read()
        print origin_data
        save_jinshujudata_to_db(origin_data)
        return origin_data

    def get_jinshujudata_from_db():
        kv = sae.kvdb.Client()
        data = kv.get('9GQgm9')
        print "get_jinshujudata_from", data
        return data

    def save_jinshujudata_to_db(data):
        kv = sae.kvdb.Client()
        key = "9GQgm9"
        value = data
        kv.add(key,value)
    
    @app.route("/weixin")
    def check_signature():
        """
        这里是验证微信Server
        """

    def parse_xml_msg():
       """
        这里是解析用户向微信公众平台发送的内容
        """

 
    @app.route("/weixin",method="POST")
    def response_weixin():
        """
        这里是响应微信Server的请求，并返回数据的主函数，判断Content内容
        如果是跟预设的值("hi")一样，就调用纯文本格式返回
        """
    #拿到并解析数据
    msg = parse_xml_msg()

    response_msg = '''\
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>1348831860</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    '''

    if msg["Content"] == "hi":
        content1 = get_jinshujudata_from_db()
        content2 = json.loads(content1)

        print "response_weixin 84",
        print "content1:",content1
        #return content1
        print msg['FromUserName']
        print msg['ToUserName']
        echo_msg = response_msg % (msg['FromUserName'],msg['ToUserName'],content2["entry"]['field_5'])
        print echo_msg
        return echo_msg
    else:
        return None



## 2. 值得注意的几个要点

1.kvdb的使用方法

官方文档在这里
http://www.sinacloud.com/doc/sae/python/kvdb.html

同时参考赖博士之前的文档

    import sae.kvdb
    count = 0 # 设置计数器
    kv = sae.kvdb.Client()

    # 将数据存进数据库
    def insert_into_db(post):
        global count
        count += 1
        ctime = time.ctime()
        key = 'key' + str(count) 
        value = {'time':ctime,'content':post}
        kv.set(key,value)

    # 读取数据库中的日记信息
    def get_all_data():
        results = []
        for item in kv.get_by_prefix('key'):
            results.append(item[1])
        return results

2.Json概述以及python对json的相关操作

参考这篇文献

http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html


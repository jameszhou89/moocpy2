# 3w课程完成篇


## 参考来源
首先参考了User Datagram Client and Server（https://pymotw.com/2/socket/udp.html）
这篇文章，主要的函数和参数都是来自于这篇。

接着参考了wp-lai的文章，感觉帮助很大。

[server--服务端 代码](https://github.com/wp-lai/OMOOC2py/blob/master/_src/om2py3w/3wex0/server/alanserver.py)

[client--客户端 代码](https://github.com/wp-lai/OMOOC2py/blob/master/_src/om2py3w/3wex0/client/alanclient.py)

同时还参考了他的gitbook，https://wp-lai.gitbooks.io/learn-python/content/1sTry/socket.html


## UDP的第一个版本

首先用 Python 完成一对最简单的 DUP 服务器/客户端。代码如下

服务端

    #server
    import socket
    import sys
    
    # Create a TCP/IP socket ~~（创建一个socket）~~
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the port~~(绑定端口)~~
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    while True:
        print >>sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(4096)~~（接受来自客户端的信息）~~
    
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        
        print >>sys.stderr, data~~（data为传输数据的名称）~~
        
        if data:
            sent = sock.sendto(data, address)~~（发送数据回到各个客户端）~~
            print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address) 




客户端




















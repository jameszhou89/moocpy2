# 3w课程完成篇1



## 参考来源
首先参考了User Datagram Client and Server（https://pymotw.com/2/socket/udp.html）
这篇文章，主要的函数和参数都是来自于这篇。

接着参考了wp-lai的文章，感觉帮助很大。

[server--服务端 代码](https://github.com/wp-lai/OMOOC2py/blob/master/_src/om2py3w/3wex0/server/alanserver.py)

[client--客户端 代码](https://github.com/wp-lai/OMOOC2py/blob/master/_src/om2py3w/3wex0/client/alanclient.py)

同时还参考了他的gitbook，https://wp-lai.gitbooks.io/learn-python/content/1sTry/socket.html


## UDP的第一个版本

首先用 Python 完成一对最简单的 DUP 服务器/客户端。

这段脚本的代码如下，能够实现的功能是：1）构建了UDP的框架 2）用户能够持续输入

服务端

    #server
    import socket
    import sys
    
    # Create a TCP/IP socket 
    ~~（创建一个socket）~~
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the port
    ~~(绑定端口)~~
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    while True:
        data, address = sock.recvfrom(4096)
        ~~（接受来自客户端的信息）~~
        ~~（data为传输数据的名称）~~
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >>sys.stderr, data
        ~~（打印接收到的数据）~~
        if data:
            sent = sock.sendto(data, address)
            ~~（发送数据回到各个客户端）~~
            print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address) 


客户端

    # Echo client program
    import socket
    import sys

    # Create a UDP socket
     ~~ (创建UDPsocket)~~
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    ~~（内网环境就用locahost,端口为10000）~~
    
    
    message=''
    ~~（先定义要传输的文件名）~~
    while True:
        b_message = raw_input('>>> ')
        ~~（持续输入的设计）~~
        if b_message=="Y":
            a_message = raw_input('>>> ')
            message += a_message + '\n'
            print >>sys.stderr, 'sending "%s"' % message
            sent = sock.sendto(message,server_address)
            ~~（发送文件/数据到服务端）~~
            # Receive response
            print >>sys.stderr, 'waiting to receive'
            data, server = sock.recvfrom(4096)
            print >>sys.stderr, 'received "%s"' % data        
            ~~（读取从服务端返回的文件）~~
        elif b_message=="N":
            break
    sock.close()



















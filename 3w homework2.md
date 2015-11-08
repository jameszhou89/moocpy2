# 3w课程完成篇2


## UDP第一个版本的缺陷
第一个版本虽然能够用，但是离作业的要求还是有很大的距离。具体表现在：

**1）收到后不能立即保存为文件**

这个可以引用1w课程的脚本，保存文件/读写文件等。如何引用（import?）

**2）如何获得历史消息？**

可以通过一个if语句，当用户输入某一个命令的时候，可以读取文件里面的历史消息


## UDP第二个版本

第二个版本总共有三个文件，server/client/jamesdiary.

第三个文件就是1w课程的脚本，里面有如何读写和保存文档的函数。服务端会引用第三个文件的函数。


### 服务端


    #server
    # -*- coding: utf-8 -*-
    import socket
    import sys
    import jamesdiary

    # 建立协议，当client发送信息为keyword时，返回所有日记历史信息
    KEYWORD = 'P'

    def response1(sock, data, address):
     ~~ (定义反应行为，如果接收到信息为KEYWORD，发回日记历史，否则则将信息记入日记)~~
    if data == 'P':
        history_message = jamesdiary.readdiary()
        ~~（读取历史文件的数据~~）
        sent = sock.sendto(history_message, address)
        ~~（把文件的历史数据送到客户端）~~
    else: 
        sent = sock.sendto(data, address)
         ~~（把当下输入的数据送到客户端）~~
        jamesdiary.writediary(data)
        ~~（把当下输入的数据更新到文件里面）~~
    
    def main():
    # Create a TCP/IP socket
    ~~（构建一个socket）~~
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    ~~(绑定socket到端口)~~
    server_address = ('localhost', 10000)
    sock.bind(server_address)
   

    while True:
        data, address = sock.recvfrom(4096)
        ~~（从客户端接受数据）~~
        if data == 'q':
            break
        response1(sock, data, address)
        ~~（进入判断语句）~~
        sock.close()

    if __name__ == '__main__':
        main()



### 客户端

    import socket
    import sys

    #建立协议，当client发送信息为keyword时，返回所有日记历史信息
    KEYWORD = 'P'

    def main():
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', 10000)
          ~~  (创建一个UDP socket)~~
        
        sock.sendto(KEYWORD,server_address)
          ~~  (发送"P"到服务端，让服务端读取文件里面所保存的数据)~~
        data, server = sock.recvfrom(4096)
          ~~  (接收服务端返回过来的文件数据)~~
        print data

  
    while True:
        b_message = raw_input('"if you want to continue print Y, want to quit print N " ')
        if b_message=="Y":
            a_message = raw_input('>>> ')
            message = a_message
          ~~  (输入一个数据)~~
            print >>sys.stderr, 'sending "%s"' % message
            sent = sock.sendto(message,server_address)
         ~~  (将此时输入的数据发送到服务端)~~
            if message=="q":
              break
            ~~  (客户端退出的机制)~~
            # Receive response
            print >>sys.stderr, 'waiting to receive'
            data, server = sock.recvfrom(4096)
            print >>sys.stderr, 'received "%s"' % data
         ~~  (接收从服务端返回过来的数据)~~
        elif b_message=="N":
            break
    sock.close()
    if __name__ == '__main__':
    main() 


### 关于jamesdiary

    import sys
    import time
    import os

    if not os.path.exists('diary.txt'):
        target= open('diary.txt', 'a')
        target.close()
    ~~（当不存在diary的文件时，自动生成一个文件）~~
    
    def writediary(data):
        target = open("diary.txt", 'a+')
        print "what do u want to say TODAY?"
        print "I'm going to write these to the file diary.txt."
        target.write(data+"  ")
        target.write(time.strftime("%Y/%m/%d%H:%M:%S"))
        target.write("\n")
    ~~ （定义写diary.txt的函数，可以被服务端所调用）~~


    def readdiary():
        target = open("diary.txt")
        return target.read()
    ~~ （定义读取diary.txt的函数，可以被服务端所调用）~~
    
    def main():
        writediary()

    if __name__ == '__main__':
        main()





















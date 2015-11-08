# 3w课程完成篇2


## UDP第一个版本的缺陷
第一个版本虽然能够用，但是离作业的要求还是有很大的距离。具体表现在：

**1）收到后不能立即保存为文件**

这个可以引用1w课程的脚本，保存文件/读写文件等。如何引用（import?）

**2）如何获得历史消息？**

可以通过一个if语句，当用户输入某一个命令的时候，可以读取文件里面的历史消息


## UDP第二个版本

第二个版本总共有三个文件，server/client/jamesdiary.

第三个文件就是1w课程的脚本，里面有如何读写和保存文档的函数。


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


























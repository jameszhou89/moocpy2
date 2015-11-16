# 4W代码1

根据之前的学习，目前的代码应该有以下功能：

1.有一个填写每天日记的表单，有一个按钮submit。


    @route('/write')
    def write():
        return '''
            <form action="/write" method="post">
                writediary: <input name="writediary1" type="text" />
                <input value="save" type="submit" />
            </form>
    '''


2.同时web会收集表单数据,保存到日记的文档。

    @route('/write', method='POST')
    def do_write():
        writediary1= request.forms.get('writediary1')
        jamesdiary.writediary(writediary1)
        if writediary1:
            return template("<p>You are now writing {{diary}} into your diary.</p>", diary=writediary1)

2.可以阅读之前的日记。

    @route("/read")
    def read():
        target = open("diary.txt")
        content=jamesdiary.readdiary()
        return content


综上所述，得到以下代码

    # -*- coding: UTF-8 -*-
    from bottle import route, run, template,debug,get,post,request
    import sys
    import time
    import os
    import jamesdiary


    @route('/write')
    def write():
        return '''
            <form action="/write" method="post">
                writediary: <input name="writediary1" type="text" />
                <input value="save" type="submit" />
            </form>
    '''


    @route('/write', method='POST')
    def do_write():
        writediary1= request.forms.get('writediary1')
        jamesdiary.writediary(writediary1)
        if writediary1:
            return template("<p>You are now writing {{diary}} into your diary.</p>", diary=writediary1)

    @route("/read")
    def read():
        target = open("diary.txt")
        content=jamesdiary.readdiary()
        return content

    debug(True)
    run(host='localhost', port=8080,debug=True)

   





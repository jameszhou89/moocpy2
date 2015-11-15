# route&template

先看一段代码

    from bottle import route, request,run,template

    @route('/login')
    def login():
        return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

    @route('/login', method='POST')
    def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username:
    	    return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    
    if __name__ == "__main__":
        run(host="localhost",port=8080,debug=True)

这里面的知识点有

1）You can bind more than one route to a single callback

2) route里加(method='POST')来跟同样路径的get行为进行区分

3) 用bottle.request.forms.get(<nametag>)来获取post的数据

4)template
http://bottlepy.org/docs/dev/tutorial.html#templates

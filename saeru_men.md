# SAE入门

1.部署本地sae-python开发环境

可以选择用pip安装
   
    $ pip install sae-python-dev
    
2.基本使用
建立index.wsgi和config.yaml两个文件
以sae官方的bottle代码为例
index.wsgi
    
    from bottle import Bottle, run
    import sae
    app = Bottle()
    @app.route('/')
    def hello():
        return "Hello, world! - Bottle"
    application = sae.create_wsgi_app(app)
    
    
    
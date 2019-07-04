from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify


# 127.0.0.1:9000?id=1&name=tom&age=20

def indexhandler(requset: Request):  # bytes, str, Response, None
    pass


def pythonhandler(requset: Request):  # bytes, str, Response, None
    pass


# 关于APP的其他写法A:
class App():
    @wsgify
    def __call__(self, request: Request):  # route, url调度
        path = request.path
        if path == '/':
            return indexhandler(request)
        elif path == '/python':
            return pythonhandler(request)
        return 'ok'


if __name__ == '__main__':
    with make_server('0.0.0.0', 9000, App()) as httpd:  # 撞见server
        print("Serving on port 9000...")
        try:
            httpd.serve_forever()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print('stop')
            httpd.server_close()

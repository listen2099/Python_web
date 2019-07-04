from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify

from webob.exc import HTTPNotFound


# 127.0.0.1:9000?id=1&name=tom&age=20

def indexhandler(requset: Request):  # bytes, str, Response, None
    return '<h1>test.com index.html</h1>'


def pythonhandler(requset: Request):  # bytes, str, Response, None
    return '<h1>test.com python</h1>'


def donothing(request: Request):
    pass


# 关于APP的其他写法A:
class App():
    _ROUTERTABLE = {
        '/': indexhandler,
        '/python': pythonhandler
    }

    @wsgify
    def __call__(self, request: Request):  # route, url调度
        path = request.path
        try:
            return self._ROUTERTABLE.get(path)(request)
        except:
            raise HTTPNotFound('<h1>not found</h1>')  # 404


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

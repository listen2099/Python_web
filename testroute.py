from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify

from webob.exc import HTTPNotFound
import logging

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


# 127.0.0.1:9000?id=1&name=tom&age=20


class Router:
    ROUTERTABLE = {}

    @classmethod
    def register(cls, path):
        def wrapper(handler):
            cls.ROUTERTABLE[path] = handler
            return handler
        return wrapper


@Router.register('/')  # fun = Router.register('/')(fun)
def indexhandler(requset: Request):  # bytes, str, Response, None
    return '<h1>test.com index.html</h1>'


@Router.register('python')
def pythonhandler(requset: Request):  # bytes, str, Response, None
    return '<h1>test.com python</h1>'


def donothing(request: Request):
    pass


# 关于APP的其他写法A:
class App:
    _Router = Router

    @wsgify
    def __call__(self, request: Request):  # route, url调度
        path = request.path
        try:
            return self._Router.ROUTERTABLE.get(path)(request)
        except Exception as e:
            logging.info(e)
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

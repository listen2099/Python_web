from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify


# 127.0.0.1:9000?id=1&name=tom&age=20


@wsgify
def app(request: Request) -> Response:  # one req one res
    return Response(b'<h1>test_text.com</h1>')
    # return b'ok also'
    # return 'en en ok also'
    # return None


# 关于APP的其他写法A:
class simple_app_A():
    @wsgify
    def __call__(self, request: Request):
        return 'ok'


# 关于APP的其他写法B:
class simple_app_B():
    def __init__(self, environ, start_response):
        for k, v in sorted(environ.items()):
            print(k, v)
        print('-' * 30)
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        self.ret = [("%s: %s\n" % (key, value)).encode("utf-8")
                    for key, value in environ.items()]

    def __iter__(self):
        yield from self.ret


if __name__ == '__main__':
    # with make_server('0.0.0.0', 9000, simple_app_A()) as httpd:  # 创建server
    with make_server('0.0.0.0', 9000, app) as httpd:  # 撞见server
        print("Serving on port 9000...")
        try:
            httpd.serve_forever()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print('stop')
            httpd.server_close()

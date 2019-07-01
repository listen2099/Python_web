from wsgiref.simple_server import make_server
import cgi
from urllib.parse import parse_qs

# 127.0.0.1:9000?id=1&name=tom&age=20

def simple_app(environ, start_response):  # 这两个参数是自动注入的
    query_string = environ.get('QUERY_STRING')  # 查询字符串
    print(query_string)
    # qs = {k: v for k, _, v in map(lambda x: x.partition('='), query_string.split('&'))}
    # qs = cgi.parse_qs(query_string)  # cgi已过期
    # print(qs)
    qs = parse_qs(query_string)  # 专门用来解析查询字符串的
    print(qs)
    method = environ.get('REQUEST_METHOD')
    print(method)
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)  # 在返回正文之前首先要返回状态码,报文头

    ret = [query_string.encode('utf-8')]
    return ret  # 这里return的是正文,必须是个可迭代对象,一般是列表,可以是一个字符串元素


# 关于APP的其他写法A:
class simple_app_A():
    def __init__(self, name, age):
        pass

    def __call__(self, environ, start_response):
        pass


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


# make_server('0.0.0.0', 9000, simple_app_A('tom', 20))
# make_server('0.0.0.0', 9000, simple_app_B)
with make_server('0.0.0.0', 9000, simple_app) as httpd:  # 撞见server
    print("Serving on port 9000...")
    httpd.serve_forever()

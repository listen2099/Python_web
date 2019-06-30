from wsgiref.simple_server import make_server, demo_app

server = make_server('0.0.0.0', 9000, demo_app)


server.serve_forever()


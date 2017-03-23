from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    from StringIO import StringIO
    stdout = StringIO()
    print >> stdout, "Hello %s" % environ['PATH_INFO'][1:]
    print >> stdout

    # h = environ.items()
    # h.sort()
    # for k, v in h:
    #     print >> stdout, k, '=', repr(v)
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return [stdout.getvalue()]


httpd = make_server('', 8000, demo_app)
sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
import webbrowser

webbrowser.open('http://localhost:8000/x')
httpd.serve_forever()  # serve one request, then exit
print dir(httpd)

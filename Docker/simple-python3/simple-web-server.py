import tornado.ioloop
import tornado.web
import socket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        user_agent = self.request.headers["User-Agent"]
        self.write("<h1>Hello from the simple-web-server Python 3 container</h1>")
        self.write("<p>I see your browser is: " + user_agent + "</p>")        
        self.write("<h2>Thanks for visiting</h2>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
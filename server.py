import json
import tornado.ioloop
import tornado.web
from src.itemtracker import ItemTracker


TRACKER = ItemTracker()
PORT = 80

class MainHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.render("index.html", args=TRACKER.get_all())

class EditHandler(tornado.web.RequestHandler):
    
    def get(self):        
        self.render("edit.html")

class CommandHandler(tornado.web.RequestHandler):
    
    def get(self):
        data = ""
        cmd = self.get_argument("cmd", None)
        sec = self.get_argument("sec", None)
        item = self.get_argument("item", None)
        print cmd, sec, item
        if cmd:
            if cmd == "get_all":
                data = TRACKER.get_all()
            elif cmd == "add_item":
                data = TRACKER.add_item(sec, item)
            elif cmd == "remove_item":
                data = TRACKER.remove_item(sec, item)
            elif cmd == "list_sections":
                data = TRACKER.list_sections()
            elif cmd == "get_section":
                data = TRACKER.get_section(sec)
        jdata = json.dumps(data)    
        self.write(jdata)
        #self.redirect("/")

if __name__ == "__main__":
    application = tornado.web.Application(
    [(r"/", MainHandler),
     (r"/command", CommandHandler),
     (r"/edit", EditHandler),
     (r"/static", tornado.web.StaticFileHandler)],
    debug=True,
    template_path="templates",
    static_path="static")
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()

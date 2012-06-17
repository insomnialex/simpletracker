from redis import Redis
from urllib import quote

RDB = Redis()

class ItemTracker(object):
    
    def __init__(self):
        pass
    
    #def add_section(self, name):
    #    RDB.hset("sections", name)
        
    @classmethod    
    def list_sections(self):
        print "list sec"
        return RDB.hkeys("sections")
        
    @classmethod    
    def add_item(self, section, item):
        print "add item"
        try:
            RDB.hset("sections", section, "exists")
            RDB.lpush(section, quote(item))
            return True
        except:
            return False
        
    @classmethod
    def remove_item(self, section, item):
        print "rem item"
        try:
            RDB.lrem(section, quote(item))
            return True
        except:
            return False
    
    @classmethod    
    def get_section(self, section):
        print "get sec"
        size = RDB.llen(section)
        return RDB.lrange(section, 0, size)
    
    @classmethod
    def get_all(self):
        print "get all"
        retVal = {}
        for section in RDB.hgetall("sections"):
            retVal[section] = self.get_section(section)
        return retVal
    
class Storage():
    def __init__(self,path):
        self.path = path
        self.keys = {}
    def get(self,name):
        if not name in self.keys:
            fh = open(self.path+"/"+name,"r")
            self.keys[name] = fh.read()
            fh.close()
        return self.key
    def set(self,name,data):
        fh = 
        fh.
        fh.close()
        
    def isSet(self):

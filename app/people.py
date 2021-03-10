from datetime import date
import cherrypy
import time
import json

@cherrypy.expose
#----------------------------------------------------------
class People_cl(object):
#----------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, db_opl, tablename, dev_type):
    #------------------------------------------------------
        self.dev_type = dev_type
        self.db_o = db_opl.getStorage_px(tablename)
        self.defaults_o = db_opl.getDefaults_px(tablename)

    #------------------------------------------------------
    def GET(self, _id = None):
    #------------------------------------------------------
        data = self.db_o.read_px()
        data = self.devTypeOnly(data)

        if _id == None:
            return json.dumps(data)
        elif str(_id) in data:
            return json.dumps(data[str(_id)]) 
        else:
            return json.dumps("INVALID ID")

    #------------------------------------------------------
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
    #------------------------------------------------------
        data = cherrypy.request.json
        self.db_o.create_px(data)
        return json.dumps("SUCCESS")
    
    #------------------------------------------------------
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def PUT(self, _id):
    #------------------------------------------------------
        data = cherrypy.request.json
        self.db_o.update_px(_id, data)
        return json.dumps("SUCCESS")

    #------------------------------------------------------
    def DELETE(self, _id):
    #------------------------------------------------------
        self.db_o.delete_px(_id)
        return json.dumps("SUCCESS")


    def devTypeOnly(self, data):
        newData = dict()
        for entry in data:
            value = data[entry]

            if value['role'] == self.dev_type:
                newData[entry] = value
        
        return newData


    
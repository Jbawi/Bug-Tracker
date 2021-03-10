from datetime import date
import cherrypy
import time
import json

@cherrypy.expose
#----------------------------------------------------------
class Bugs_cl(object):
#----------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, db_opl, tablename):
    #------------------------------------------------------
        self.db_o = db_opl.getStorage_px(tablename)
        self.defaults_o = db_opl.getDefaults_px(tablename)

    #------------------------------------------------------
    def GET(self, _id = None, progress = None):
    #------------------------------------------------------
        data = self.db_o.read_px()

        if _id == None and progress == None:
            return json.dumps(data)
        elif str(_id) in data and progress == None:
            return json.dumps(data[str(_id)])
        elif progress != None and _id == None:
            if progress == "solved":
                return json.dumps(self.solvedOnly(data))
            elif progress == "detected":
                return json.dumps(self.detectedOnly(data))
            else:
                return json.dumps("INVALID PROGRESS ATTRIBUTE")
        else:
            return json.dumps("INVALID ID OR INVALID REQUEST")

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

    def solvedOnly(self, data):
        newData = dict()
        for entry in data:
            value = data[entry]

            if value['bugStatus'] == "4":
                newData[entry] = value

        return newData

    def detectedOnly(self, data):
        newData = dict()
        for entry in data:
            value = data[entry]

            if int(value['bugStatus']) < 4 and int(value['bugStatus']) > 0:
                newData[entry] = value

        return newData
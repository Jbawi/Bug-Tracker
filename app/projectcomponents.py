from datetime import date
import cherrypy
import time
import json

@cherrypy.expose
#----------------------------------------------------------
class ProjectComponents_cl(object):
#----------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, db_opl, tablename):
    #------------------------------------------------------
        self.db_o = db_opl.getStorage_px(tablename)
        self.defaults_o = db_opl.getDefaults_px(tablename)

    #------------------------------------------------------
    def GET(self, _id):
    #------------------------------------------------------
        data = self.db_o.read_px()

        newData = dict()
        for entry in data:
            value = data[entry]

            if str(value['project_id']) == str(_id):
                newData[entry] = value
        
        return json.dumps(newData)


    
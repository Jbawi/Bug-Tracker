import cherrypy
import json
import datetime
from . import projectcomponents
from . import bugs

@cherrypy.expose
#----------------------------------------------------------
class Timedif_cl(object):
#----------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, projects, components, bugs):
    #------------------------------------------------------
        self.projects = projects
        self.components = components
        self.bugs = bugs

    #------------------------------------------------------
    def GET(self):
    #------------------------------------------------------
        projects = json.loads(self.projects.GET())
        data = dict()
        for project in projects:
            comp = json.loads(self.components.GET(project))
        
            bugsSolved = json.loads(self.bugs.GET(progress = "solved"))

            for component in comp:

                comp[component]["bugsSolved"] = dict()

                for bug in bugsSolved:
                    currBug = bugsSolved[bug]
                    if int(currBug['component_id']) == int(component):
                        comp[component]["bugsSolved"][bug] = currBug
                
                comp[component]["bugsSolved"] = self.sortByTimeDif(comp[component]["bugsSolved"])
            
            data[project] = {
                "project": projects[project]["name"],
                "components": comp
            }

        return json.dumps(data)
    
    #------------------------------------------------------
    def sortByTimeDif(self, data):
    #------------------------------------------------------
        newData = []

        for key in data: 
            foundAt = datetime.datetime.strptime(data[key]["foundAtDate"], "%Y-%m-%d")
            solvedAt = datetime.datetime.strptime(data[key]["solvedAtDate"], "%Y-%m-%d")
            difference = solvedAt - foundAt
            data[key]["difference"] = int(difference.days)
            data[key]["id"] = key
            newData.append(data[key])

        newData = sorted(newData, key=lambda k: k["difference"])
        finishedData = dict()

        for key in newData:
            finishedData[key["id"]] = key

        return finishedData

import cherrypy
import json
from . import projectcomponents
from . import bugs

@cherrypy.expose
#----------------------------------------------------------
class Prolist_cl(object):
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
            bugsDetected = json.loads(self.bugs.GET(progress = "detected"))
        
            for component in comp:

                comp[component]["bugsSolved"] = dict()
                for bug in bugsSolved:
                    currBug = bugsSolved[bug]
                    if int(currBug['component_id']) == int(component):
                        comp[component]["bugsSolved"][bug] = currBug
                
                comp[component]["bugsDetected"] = dict()
                for bug in bugsDetected:
                    currBug = bugsDetected[bug]
                    if int(currBug['component_id']) == int(component):
                        comp[component]["bugsDetected"][bug] = currBug
            
            data[project] = {
                "project": projects[project]["name"],
                "components": comp
            }

        return json.dumps(data)


    
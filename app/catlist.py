import cherrypy
import json
from . import projectcomponents
from . import bugs

@cherrypy.expose
#----------------------------------------------------------
class Catlist_cl(object):
#----------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, category, bugs):
    #------------------------------------------------------
        self.category = category
        self.bugs = bugs

    #------------------------------------------------------
    def GET(self):
    #------------------------------------------------------
        cat = json.loads(self.category.GET())
    
        bugsSolved = json.loads(self.bugs.GET(progress = "solved"))
        bugsDetected = json.loads(self.bugs.GET(progress = "detected"))
    
        for category in cat:

            cat[category]["bugsSolved"] = dict()
            for bug in bugsSolved:
                currBug = bugsSolved[bug]
                if int(currBug['component_id']) == int(category):
                    cat[category]["bugsSolved"][bug] = currBug
            
            cat[category]["bugsDetected"] = dict()
            for bug in bugsDetected:
                currBug = bugsDetected[bug]
                if int(currBug['category_id']) == int(category):
                    cat[category]["bugsDetected"][bug] = currBug

        return json.dumps(cat)


    
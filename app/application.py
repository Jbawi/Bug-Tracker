import cherrypy

from . import database
from . import projects
from . import components
from . import people
from . import bugs
from . import categories
from . import projectcomponents
from . import prolist
from . import catlist
from . import timedif

@cherrypy.expose
#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

    #------------------------------------------------------
    def __init__(self, currDir_spl):
    #------------------------------------------------------
        self.db_o = database.Database_cl(currDir_spl)

        self.projects = projects.Projects_cl(self.db_o, "projects")
        self.components = components.Components_cl(self.db_o, "components")
        self.projectcomponents = projectcomponents.ProjectComponents_cl(self.db_o, "components")
        self.qsemployee = people.People_cl(self.db_o, "devs", "QS-Mitarbeiter")
        self.swengineer = people.People_cl(self.db_o, "devs", "SW-Entwickler")
        self.bugs = bugs.Bugs_cl(self.db_o, "bugs")
        self.caterror = categories.Categories_cl(self.db_o, "catError")
        self.catcause = categories.Categories_cl(self.db_o, "catCause")

        #Auswertungen
        self.prolist = prolist.Prolist_cl(self.projects, self.projectcomponents, self.bugs)
        self.catlist = catlist.Catlist_cl(self.caterror, self.bugs)
        self.timedif = timedif.Timedif_cl(self.projects, self.projectcomponents, self.bugs)
import sys
import os
import cherrypy
from app import application
cherrypy.config.update({'server.socket_port': 8083})
def main():
    # Get current directory
    currDir_s = sys.path[0]

    # Configuration for the API
    API_CONf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        }
    }

    # Configuration for the static mainpage
    CONF = {
        '/': {
            'tools.staticdir.root': currDir_s,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './content',
            'tools.staticdir.index': '../templates/index.html'
        }
    }

    cherrypy.tree.mount(None, '/', CONF)
    cherrypy.tree.mount(application.Application_cl(currDir_s), '/api', API_CONf)

    cherrypy.engine.start()
    cherrypy.engine.block()
#--------------------------------------
if __name__ == '__main__':
#--------------------------------------
    main()
# EOF
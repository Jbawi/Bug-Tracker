#--------------------------------------
# WEB 2019/2020
# Aufgabe P2 / Anwendungsrahmen
#--------------------------------------

import os
import os.path
import codecs
import json

from . import dataid
from . import storage

#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------

    #-------------------------------------------------------
    def __init__(self, currDir_spl):
    #-------------------------------------------------------
        self.maxId_o = dict()
        self.maxId_o["bugs"] = dataid.DataId_cl(currDir_spl, "bugs")
        self.maxId_o["components"] = dataid.DataId_cl(currDir_spl, "components")
        self.maxId_o["devs"] = dataid.DataId_cl(currDir_spl, "devs")
        self.maxId_o["projects"] = dataid.DataId_cl(currDir_spl, "projects")
        self.maxId_o["catCause"] = dataid.DataId_cl(currDir_spl, "catCause")
        self.maxId_o["catError"] = dataid.DataId_cl(currDir_spl, "catError")

        self.types_o = {
            'bugs': {
                'storage': storage.Storage_cl('bugs', currDir_spl, self.maxId_o['bugs']),
                'defaults': {
                    "description": "",
                    "discoverer_id": "",
                    "foundAtDate": "",
                    "qs_id": "1",
                    "category": "",
                    "se_id": "",
                    "solution": "",
                    "solvedAtDate": "",
                    "causeOfError": "",
                    "bugStatus": "1"
                }
            },
            'components': {
                'storage': storage.Storage_cl('components', currDir_spl, self.maxId_o['components']),
                'defaults': {
                    "project_id": "",
                    "title": ""
                }
            },
            'devs': {
                'storage': storage.Storage_cl('devs', currDir_spl, self.maxId_o['devs']),
                'defaults': {
                    "name": "",
                    "role": ""
                }
            },
            'projects': {
                'storage': storage.Storage_cl('projects', currDir_spl, self.maxId_o['projects']),
                'defaults': {
                    "name": "",
                    "description": ""
                }
            },
            'catCause': {
                'storage': storage.Storage_cl('catCause', currDir_spl, self.maxId_o['catCause']),
                'defaults': {
                    "type": ""
                }
            },
            'catError': {
                'storage': storage.Storage_cl('catError', currDir_spl, self.maxId_o['catCause']),
                'defaults': {
                    "type": ""
                }
            }
        }

    #-------------------------------------------------------
    def getStorage_px(self, type_spl):
    #-------------------------------------------------------
        storage_o = None
        if type_spl in self.types_o:
            storage_o = self.types_o[type_spl]['storage']
        return storage_o

    #-------------------------------------------------------
    def getDefaults_px(self, type_spl):
    #-------------------------------------------------------
        defaults_o = None
        if type_spl in self.types_o:
            defaults_o = self.types_o[type_spl]['defaults']
        return defaults_o

# EOF
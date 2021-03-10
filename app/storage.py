import os
import os.path
import codecs
import json

#----------------------------------------------------------
class Storage_cl(object):
#----------------------------------------------------------
   
   #-------------------------------------------------------
   def __init__(self, type_spl, currDir_spl, idCounter_opl):
   #-------------------------------------------------------
      self.type_s = type_spl
      self.currDir_s = currDir_spl
      self.data_o = None
      self.maxId_o = idCounter_opl
      self.readData_p()

   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------
      id_s = self.maxId_o.create_px()
      self.data_o[id_s] = data_opl
      self.saveData_p()
      return id_s

   #-------------------------------------------------------
   def read_px(self, id_spl = None):
   #-------------------------------------------------------
      data_o = None
      if id_spl == None:
         data_o = self.data_o
      else:
         if id_spl in self.data_o:
               data_o = self.data_o[id_spl]
      return data_o

   #-------------------------------------------------------
   def update_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      status_b = False
      if id_spl in self.data_o:
         self.data_o[id_spl] = data_opl
         self.saveData_p()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_px(self, id_spl):
   #-------------------------------------------------------
      status_b = False
      if id_spl in self.data_o:
         del self.data_o[id_spl]
         self.saveData_p()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open(os.path.join(self.currDir_s, 'data', self.type_s + '.json'), 'r', 'utf-8')
      except:
         self.data_o = {}
         self.saveData_p()
      else:
         with fp_o:
            self.data_o = json.load(fp_o)
      return

   #-------------------------------------------------------
   def saveData_p(self):
   #-------------------------------------------------------
      with codecs.open(os.path.join(self.currDir_s, 'data', self.type_s + '.json'), 'w', 'utf-8') as fp_o:
         json.dump(self.data_o, fp_o, indent=3)

# EOF
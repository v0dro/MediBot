#!usr/bin/python
#DATES : 4JAN15 , ___?___ 
#DISPATCHER : called by server.py.
#USE : To read DICT object , and assign it to correct core object . 
#FUNCTIONS:  
#Owner : Jaideep Kekre 
#Issues: "Sameer put your issues here"

import core

# @author Sameer Deshmukh / Jaideep Kekre 
class dispatcher():
  """
  class called by a thread that gets a dict and talks to core for 
  further processing.
  """
  def __init__(self):
    self.object_list=dict()
    #dict to store active objects and map them to users

    pass
  
  #@author Jaideep 
  def dispatch_to_core(self,arg_dict):
    messageDict=arg_dict
    #dispatching logic goes here
    for user in self.object_list:
        
      if (user == messageDict['chat_id']):
        print "\n\n\n" + user + " found! , reusing object\n"
        core_obj=self.object_list[user]
        response_dict=core_obj.run_core(messageDict)
        return response_dict 

      
    print str(messageDict['chat_id']) + " not found , creating new object "
    coreobj=core.core(messageDict['chat_id'])
    self.object_list[messageDict['chat_id']]=coreobj
    #stores created object in class variable for future use. 
    response_dict=coreobj.run_core(messageDict)
    return response_dict

  def run_dispatcher(self,arg_dict):
    #called by server() 
    #scaffolding code 
    response_dict = self.dispatch_to_core(arg_dict)
    #returned to server()
    #response dict has field 'chat_id' 'response_list'
    #logging
    print "\ninput is :"  + str(arg_dict)
    print "response is :" + str(response_dict)
    print self.object_list  
    return response_dict 


def main():
  sampleDict=dict();
  sampleDict={'chat_id':'desh' ,'text' : 'yo yo yo GTFO!'}
  sampleDispatch=dispatcher()
  sampleDispatch.run_dispatcher(sampleDict)
  sampleDispatch.run_dispatcher(sampleDict)
  sampleDict={'chat_id':'Kekre' ,'text' : 'yo yo yo GTFO!'}
  sampleDispatch.run_dispatcher(sampleDict)
  sampleDispatch.run_dispatcher(sampleDict)
   



if __name__ == '__main__':
	main()


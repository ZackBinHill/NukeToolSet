# -*- coding: utf-8 -*-
# Author: Zack Zhou 
# Created on: 2016.05.14   13:53:24

# Import 
import os
import nuke
import nukescripts

# Function
def log_(string):    
    sys.stdout.write("DEBUG: {0}\n".format( str(string)) )
    sys.stdout.flush()

def custom_create_read(defaulttype="Read"): 

    '''Create a Read node for a file selected from the file browser. 
    If a node is currently selected in the nodegraph and it has a 'file' 
    (or failing that a 'proxy') knob, the value (if any) will be used as the default 
    path for the file browser.''' 
    # Get the selected node, and the path on it's 'file' knob if it 
    # has one, or failing that, it's 'proxy' node, if it has that. 
    sel_node = None 
    default_dir = None 
    try: 
      sel_node = nuke.selectedNode() 
    except: 
      pass 
    if ( sel_node is not None ) and ( sel_node != '' ): 
      if 'file' in sel_node.knobs(): 
        default_dir = sel_node['file'].value() 
      if (default_dir == None or default_dir == '') and 'proxy' in sel_node.knobs(): 
        default_dir = sel_node['proxy'].value() 
     
    # Revert default_dir to None if it's empty so that the file browser 
    # will do it's default unset behaviour rather than open on an empty path. 
    if default_dir == '': default_dir = None 
     
    # Raise the file browser and get path(s) for Read node(s). 
    files = nuke.getClipname( "Read File(s)", default=default_dir, multiple=True ) 
    if files != None: 
        maxFiles = nuke.numvalue("preferences.maxPanels") 
        n = len(files) 
        for f in files: 
        	log_(f)
	        isAbc = False 
	        stripped = nuke.stripFrameRange(f) 
	        nodeType = defaulttype 
	        if isAudioFilename( f ): 
	          nodeType = "AudioRead" 
	        if isGeoFilename( f ): 
	          nodeType = "ReadGeo2" 
	        if isAbcFilename( f ): 
	          isAbc = True 
	        if isDeepFilename( f ): 
	          nodeType = "DeepRead" 
	           
	        # only specify inpanel for the last n nodes. Old panels are kicked out using 
	        # a deferred delete, so reading large numbers of files can internally build  
	        # large numbers of active widgets before the deferred deletes occur. 
	        useInPanel = True 
	        if (maxFiles != 0 and n > maxFiles): 
	          useInPanel = False      
	        n = n-1 
	         
	        if isAbc: 
	          nuke.createScenefileBrowser( f, "" ) 
	        else: 
	          try: 
	            nuke.createNode( nodeType, "file {"+f+"}", inpanel = useInPanel) 
	          except RuntimeError, err: 
	            nuke.message(err.args[0]) 



def isGeoFilename(filename): 

    filenameLower = filename.lower() 
    _, ext = os.path.splitext( filenameLower ) 
     
    if ext in ['.fbx', '.obj']: 
      return True 
    else: 
      return False 

   
def isAbcFilename(filename): 

    filenameLower = filename.lower() 
    _, ext = os.path.splitext( filenameLower ) 
     
    if ext in ['.abc']: 
      return True 
    else: 
      return False 

   
def isDeepFilename(filename): 

    filenameLower = filename.lower() 
    _, ext = os.path.splitext( filenameLower ) 
     
    if ext in ['.dtex', '.dshd', '.deepshad']: 
      return True 
    else: 
      return False 

      
def isAudioFilename(filename): 

    filenameLower = filename.lower() 
    _, ext = os.path.splitext( filenameLower ) 
     
    if ext in ['.wav', '.wave', '.aif', '.aiff']: 
      return True 
    else: 
      return False 


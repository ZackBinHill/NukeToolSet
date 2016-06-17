# -*- coding: utf-8 -*-
# Author: Zack Zhou
# Created on: 2016.05.16 21:25:36 

# Import
import os
import sys
import nuke
import nukescripts

# Function 
def log_(string):    
    sys.stdout.write("DEBUG: {0}\n".format( str(string)) )
    sys.stdout.flush()

def FileHandler( dropdata ):
	filePath = dropdata
	if os.path.basename(filePath).startswith('.') or os.path.basename(filePath).endswith('~'):
		return
	log_( filePath )
	fileRange = ''

	if not os.path.isfile(filePath):
		filePath, sep, fileRange = filePath.rpartition(' ')

 	fileName, fileExt = os.path.splitext(filePath)
 	fileExt = fileExt.lower()

 	if fileExt == '.obj':
 		r = nuke.createNode("ReadGeo2", inpanel=False)		
 		r['file'].fromUserText(dropdata)
 		#r['file'].setValue(dropdata)
 		r['selected'].setValue(0)
 		return

 	if fileExt == '.fbx':
 		r = nuke.createNode("ReadGeo2", inpanel=False)	
 		r['file'].fromUserText(dropdata)
 		r['all_objects'].setValue(True)
 		r['selected'].setValue(0)
 		nuke.tprint(dropdata)	

 		camNode = nuke.createNode('Camera2', 'read_from_file 1 file '+dropdata, inpanel=True)
		#c = nuke.createNode('Camera2', inpanel=True)
		#c['read_from_file'].setValue(1)
		#c['file'].setValue(dropdata)
		camNode['fbx_node_name'].setValue(7)
 		camNode['selected'].setValue(0)
 		return

 	if fileExt == '.abc':
   		try:
   			r = nuke.createNode('ReadGeo2', inpanel=False) 			
   			r['file'].fromUserText(dropdata)
   			r['read_on_each_frame'].setValue(1)
   			r['sub_frame'].setValue(1)
   			r['selected'].setValue(0)
   			return
   		except Exception, e:
   			log_('DEBUG: NUKE_VERSION_MAJOR > 7? %s' % e)


 	if fileExt == '.3dl' or fileExt == '.blur' or fileExt == '.csp' or fileExt == '.cub' or fileExt == '.cube' or fileExt == '.vf' or fileExt == '.vfz':
 		r = nuke.createNode('Vectorfield', inpanel=False)
 		r['vfield_file'].setValue(dropdata)
 		r['selected'].setValue(0)
 		return

 	if fileExt == '.chan':
 		r = nuke.createNode('Camera2', inpanel=False)
 		nuke.tcl('in %s {import_chan_file %s}' %(r.name(), dropdata))
 		r['selected'].setValue(0)
 		return

 	if fileExt == '.nk':
 		try:
 			r = nuke.nodePaste(dropdata)
 		except Exception, e:
 			log_('Error %s' % e)
			pass
 		return

 	if fileExt == '.py':
 		try:
 			r = nuke.load(dropdata) 
 		except Exception, e:
 			log_('Error %s' % e)
			pass
 		return

   	if fileExt in (None, False, '', '.db', '.sni', '.ma', '.mb', '.hip', '.sfx', '.xml', '.pkl', '.tmp', 'otl'):
   		log_('Ignore')
   		return

   	r = nuke.createNode('Read', "file {"+dropdata+"}", inpanel=False)
   	return


def PathHandler( dropdata ):
	value = dropdata
	if os.path.isdir(value):
		recurse = True

		validList = nuke.getFileNameList(value, False, bool(recurse), False)
		if validList:
			for each in validList:
				data = os.path.join(str(value), str(each))
				try:
					PathHandler(data)
				except Exception, e:
					log_('Error: %s' % e)
					pass
	else:
		FileHandler(dropdata)

def DropHandler(droptype, dropdata):
	if ('sel cut_paste_input' in dropdata):
		log_('paste date')
		return False

	elif ('\n' in dropdata):
		dropdatalist = [i.strip() for i in dropdata.split('\n') if i]
		log_( dropdatalist )
		for i in dropdatalist:
			if os.path.isfile(i) or os.path.isdir(i):
				PathHandler(i)         # import file to node graph #

			else:
				log_('Files Error')
				return False

	else:
		dropdata = dropdata.strip()
		log_( dropdata)
		if os.path.isfile(dropdata) or os.path.isdir(dropdata):
			PathHandler(dropdata)      # import file to node graph #
		else:
			log_('Files Error')
			return False
	return True
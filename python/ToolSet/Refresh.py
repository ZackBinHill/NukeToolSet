# -*- coding: utf-8 -*-
# Author: zack Bin
# Created on: 2016.05.19 23:40:32

# Import 
import os
import nuke
import command, config
from init import cgspread_root_path

# Function
def refresh():
	toolbar = nuke.menu('Nodes')
	cgspread_menu = toolbar.addMenu('cgspread', os.path.join(cgspread_root_path, 'icons/icon_menu/logo.png'))
	cgspread_menu.clearMenu()

	# reload module
	reload(command)
	reload(config)

	cgspread_menu.addCommand('refresh', "execfile(os.path.join(cgspread_root_path,'python/ToolSet/Refresh.py'))")
	cgspread_menu.addCommand('-', '', '')

	#execfile(os.path.join(cgspread_root_path, 'menu.py'))

refresh()

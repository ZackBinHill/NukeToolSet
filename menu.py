# -*- coding: utf-8 -*-
# Author: Zack Zhou
# Created on: 2016.05.16 21:25:36 

# Import
import nuke
import nukescripts
from cdd_handler import DropHandler
from custom_create_read import custom_create_read

# Function 
nukescripts.addDropDataCallback(DropHandler)

nukescripts.create_read = custom_create_read

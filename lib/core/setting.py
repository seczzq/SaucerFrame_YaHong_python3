#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright (c) saucerman (https://saucer-man.com)
See the file 'LICENSE' for copying permission
"""
import sys
import os

GIT_REPOSITORY = "https://github.com/saucer-man/saucerframe"
WEBSITE = "https://saucer-man.com"
BANNER = r"""
  _____                       _     _____                                 
 |_   _|                     | |   / ____|                                
   | |  _ __   __ _  ___  ___| | _| (___   ___ __ _ _ __  _ __   ___ _ __ 
   | | | '_ \ / _` |/ _ \/ _ \ |/ /\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  _| |_| | | | (_| |  __/  __/   < ____) | (_| (_| | | | | | | |  __/ |   
 |_____|_| |_|\__, |\___|\___|_|\_\_____/ \___\__,_|_| |_|_| |_|\___|_|   
               __/ |                                                      
              |___/                                                       
""".format(website=WEBSITE)

# essential methods/functions in custom scripts/PoC (such as function poc())
ESSENTIAL_MODULE_METHODS = 'poc'

IS_WIN = True if (sys.platform in ["win32", "cygwin"] or os.name == "nt") else False
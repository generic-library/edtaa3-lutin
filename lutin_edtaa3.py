#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "edtaa3 library (create distance field from image)"

def create(target):
	# module name is 'edn' and type binary.
	myModule = module.Module(__file__, 'edtaa3', 'LIBRARY')
	# add the file to compile:
	myModule.add_src_file([
		'edtaa3/edtaa3func.c'
		])
	myModule.compile_version_CC(1999)
	myModule.add_export_path(tools.get_current_path(__file__))
	return myModule



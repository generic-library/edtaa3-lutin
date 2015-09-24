#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "edtaa3 library (create distance field from image)"

def create(target):
	# module name is 'edn' and type binary.
	my_module = module.Module(__file__, 'edtaa3', 'LIBRARY')
	# add the file to compile:
	my_module.add_src_file([
		'edtaa3/edtaa3func.c'
		])
	my_module.add_header_file([
		'edtaa3/edtaa3func.h'
		])
	my_module.compile_version_CC(1999)
	my_module.add_path(tools.get_current_path(__file__))
	return my_module



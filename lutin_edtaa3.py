#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "edtaa3 library (create distance field from image)"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["Stefan Gustavson <stefan.gustavson@gmail.com>"]

def get_version():
	return [0,5]

def configure(target, my_module):
	my_module.add_src_file([
	    'edtaa3/edtaa3func.c'
	    ])
	my_module.add_header_file([
	    'edtaa3/edtaa3func.h'
	    ])
	my_module.compile_version("C", 1999)
	my_module.add_depend([
	    'c',
	    'm'
	    ])
	return True



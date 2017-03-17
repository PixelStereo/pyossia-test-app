#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of a device
with I/O communication provided by libossia
"""

# append pyossia path
import sys, os
sys.path.append(os.path.abspath(".."))

from pyossia import *

# create the OSSIA Device with the name provided
# here for test purpose
my_device = ossia.LocalDevice('PyOssia Device')
my_device.expose(protocol='oscquery', udp_port=3456, ws_port=5678)
my_int = my_device.add_param('test/value/int', datatype='int')
my_float = my_device.add_param('test/value/float', datatype='float')
my_bool = my_device.add_param('test/value/bool', datatype='bool')
my_string = my_device.add_param('test/value/string', datatype='string')
my_string.push_value(ossia.Value(" Supa String !!"))
my_bool.push_value(ossia.Value(True))
my_float.push_value(ossia.Value(2.22))
my_int.push_value(ossia.Value(222))
my_string.push_value(ossia.Value('hello world!'))



# my_device = ossia.LocalDevice('PyOssia Device')
# add param will create a python property called my_string
# my_string wiil be created in the current LocalDecice instance
# this magic enhancement will be done by my_string
# is it possible to create a property in a class generated by pybind?
# other solution is to wrap code into a 
# my_string = my_device.add_param('test/value/string', datatype='string')
# my_device.my_string = 'hello world!'
# print(my_device.my_string)

while True:
	pass
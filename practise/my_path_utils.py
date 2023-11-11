#!/bin/env python
#-*- encoding=utf8 -*-

import os,sys

print(__file__)
print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))

print(os.path.dirname(__file__))


print("sys.path={}".format(sys.path))
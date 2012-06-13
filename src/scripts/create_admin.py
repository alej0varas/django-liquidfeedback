#!/bin/env python

#-----------------------------------------------------------------------------
# Name:        create_admin.py
# Purpose:     auto generate django admin.py from models.py
#
# Author:      Alejandro Varas<alej0varas@gmail.com>
#
# Created:     <2012-06-13 Wed>
# Copyright:   (c) 2012
# Licence:     GPL
#-----------------------------------------------------------------------------

import os
import sys

assert len(sys.argv) == 3, "usage: create_admin.py project_name app_name"
prjname, appname = sys.argv[1:]

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, PROJECT_ROOT)

import os
os.environ['DJANGO_SETTINGS_MODULE'] = prjname + '.settings'

exec "from %s import models" % (appname)

fp = open(os.path.join(PROJECT_ROOT, "%s/admin.py" % (appname)), "w")

print >> fp,  '''#coding: utf-8
from django.contrib import admin
from %s.models import *
''' % (appname)

for name, klazz in models.__dict__.items():
    if isinstance(klazz, type) and issubclass(klazz, models.models.Model):
        #print name, klazz
        print >> fp, "admin.site.register(%s)" % (name)

        # if hasattr(klazz, 'Admin'):
        #     print >> fp,  'class %sAdmin(admin.ModelAdmin):' % name
        #     #print dir(klazz.Admin)
        #     attrs = [(k, v) for k, v in klazz.Admin.__dict__.items() if k[0] != '_']
        #     if len(attrs):
        #         for k, v in attrs:
        #             if k=='fields':
        #                 k = 'fieldsets'
        #             print >> fp, "\t%s=%s" % (k, repr(v).encode('utf-8'))
        #     else:
        #         print >> fp, "\tpass"
        #     print >> fp, "admin.site.register(%s, %sAdmin)" % (name, name)
        #     print >> fp

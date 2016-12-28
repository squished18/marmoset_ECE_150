#!/usr/bin/env python

from subprocess import Popen, PIPE
import commands
import sys

cproc = Popen("./BasicGraphics", stdout=PIPE)
firstline = cproc.stdout.readline()
for count in xrange(2,20):
	dummyline = cproc.stdout.readline()
lastline = cproc.stdout.readline()

if ("----------------------------------------------------------------------" in firstline) and ("----------------------------------------------------------------------" in lastline):
    print "passed"
    sys.exit(0)
print "failed"
sys.exit(1)

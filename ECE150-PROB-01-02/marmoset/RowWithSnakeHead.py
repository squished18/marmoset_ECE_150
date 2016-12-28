#!/usr/bin/env python

from subprocess import Popen, PIPE
import commands
import sys

cproc = Popen("./BasicGraphics", stdout=PIPE)
for count in xrange(1,7):
	dummyline = cproc.stdout.readline()
currline = cproc.stdout.readline()
if not "| **********O                                                        |" in currline:
	print "failed"
	sys.exit(1)
print "passed"
sys.exit(0)

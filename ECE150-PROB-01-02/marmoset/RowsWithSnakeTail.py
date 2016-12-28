#!/usr/bin/env python

from subprocess import Popen, PIPE
import commands
import sys

cproc = Popen("./BasicGraphics", stdout=PIPE)
dummyline = cproc.stdout.readline()
for count in xrange(1,6):
	currline = cproc.stdout.readline()
	if not "| *                                                                  |" in currline:
		print "failed"
		sys.exit(1)
print "passed"
sys.exit(0)

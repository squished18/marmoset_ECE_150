#!/usr/bin/env python

from subprocess import Popen, PIPE
import commands
import sys

cproc = Popen("./BasicGraphics", stdout=PIPE)
for count in xrange(0,7):
	dummyline = cproc.stdout.readline()
for count in xrange(8,20):
	currline = cproc.stdout.readline()
	if not "|                                                                    |" in currline:
		print "failed"
		sys.exit(1)
print "passed"
sys.exit(0)

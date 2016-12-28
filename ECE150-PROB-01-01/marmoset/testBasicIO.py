#!/usr/bin/env python

from subprocess import Popen, PIPE
import commands
import sys

# First test (String check)
searchfile = open("BasicIO.cpp", "r")
for line in searchfile:
    if "string" in line: 
		print "failed"
		sys.exit(1)
searchfile.close()

# Other tests (IO validity checks)
input = "Test-StringLength19 311299 999999999 Test-StringLength19 Test-StringLength19 Test-StringLength19 Test-StringLength19"
cproc = Popen("./BasicIO", stdin=PIPE, stdout=PIPE)
out, err = cproc.communicate(input)
if ("Test-StringLength19" in out) and ("311299" in out) and ("999999999" in out):
    print "passed"
    sys.exit(0)
print "failed"
sys.exit(1)
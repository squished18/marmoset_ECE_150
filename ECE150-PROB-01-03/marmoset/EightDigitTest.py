#!/usr/bin/env python

from subprocess import Popen, PIPE
import commands
import sys

# First test (String check)
searchfile = open("passcode.cpp", "r")
for line in searchfile:
    if "string" in line: 
		print "failed - the word 'string' found in code"
		sys.exit(1)
searchfile.close()

# Other tests (IO validity checks)
input = "Doe"
cproc = Popen("./passcode", stdin=PIPE, stdout=PIPE)
out, err = cproc.communicate(input)
if ("68111101" in out):
    print "passed"
    sys.exit(0)
print "failed"
sys.exit(1)
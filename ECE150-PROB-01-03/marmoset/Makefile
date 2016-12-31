LDFLAGS = -g 
CFLAGS = -Wall -g -ansi -Werror
CC = g++

PUBLIC_TESTS = EightDigitTest.py NineDigitTest.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = passcode.cpp

all:	clean $(ALL_TESTS) passcode
	chmod +x $(ALL_TESTS) passcode

clean:
	/bin/rm -rf *.o passcode

passcode.o: passcode.cpp
	$(CC) -c $(LDFLAGS) $<

passcode: passcode.o
	$(CC) $< -o $@

check:	passcode.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"

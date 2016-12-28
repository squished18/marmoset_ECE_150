LDFLAGS = -g 
CFLAGS = -Wall -g -ansi -Werror
CC = g++

PUBLIC_TESTS = testBasicIO.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = BasicIO.cpp

all:	clean $(ALL_TESTS) BasicIO
	chmod +x $(ALL_TESTS) BasicIO

clean:
	/bin/rm -rf *.o BasicIO

BasicIO.o: BasicIO.cpp
	$(CC) -c $(LDFLAGS) $<

BasicIO: BasicIO.o
	$(CC) $< -o $@

check:	BasicIO.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"

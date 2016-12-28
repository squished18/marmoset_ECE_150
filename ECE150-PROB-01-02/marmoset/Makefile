LDFLAGS = -g 
CFLAGS = -Wall -g -ansi -Werror
CC = g++

PUBLIC_TESTS = TopBottomWall.py RowsWithSnakeTail.py RowWithSnakeHead.py OtherSideWalls.py
RELEASE_TESTS =
SECRET_TESTS =
ALL_TESTS = $(PUBLIC_TESTS) $(RELEASE_TESTS) $(SECRET_TESTS)

EXE = BasicGraphics.cpp

all:	clean $(ALL_TESTS) BasicGraphics
	chmod +x $(ALL_TESTS) BasicGraphics

clean:
	/bin/rm -rf *.o BasicGraphics

BasicGraphics.o: BasicGraphics.cpp
	$(CC) -c $(LDFLAGS) $<

BasicGraphics: BasicGraphics.o
	$(CC) $< -o $@

check:	BasicGraphics.o
	echo $<
	echo $@
	echo "public: $(PUBLIC_TESTS)"
	echo "release: $(RELEASE_TESTS)"

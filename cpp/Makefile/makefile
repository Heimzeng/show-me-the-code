DIR_BIN = ./bin
DIR_SRC = ./src
DIR_INC = ./include
DIR_OBJ = ./obj

CC = gcc
CFLAGS = -g -Wall

objects = ./src/test.o ./src/main.o

main : $(objects)
  gcc -o main $(objects)

main.o : ./src/main.cpp 
test.o : ./src/test.cpp ./src/test.h

clean :
  rm main $(objects)

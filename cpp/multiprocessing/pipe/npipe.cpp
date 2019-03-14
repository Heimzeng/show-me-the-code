#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h> 
#include <sys/stat.h> 
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  char filename[] = "test_fifo";
  if (!mkfifo(filename,S_IRUSR | S_IWUSR| S_IRGRP|S_IWGRP)){
    pid_t pid = fork();
    if (pid == 0){  //child
      int fd = open(filename, O_WRONLY);
      if (fd < 0)
  perror("child open()");
      else{
  if (strlen(argv[1]) != write(fd, argv[1], strlen(argv[1])))
    perror("child write error");
  else
    close(fd);
      }
    }
    else if (pid > 0){  //father
      int fd = open(filename, O_RDONLY);
      if (fd < 0)
  perror("father open()");
      else{
  char buffer[200];
  int readed = read(fd, buffer, 199);
  close(fd);
  buffer[readed] = '\0';
  printf("%s\n",buffer);
      }
    }
    else
      perror("fork()");
  }
  else
    perror("mkfifo() error:");
}
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char** argv) {
  size_t memory_size = 8 * 1024 * 1024;
  if (argc > 0 && strstr(argv[0], "plain-small") != NULL) {
    memory_size = 4 * 1024 * 1024;
  }
  void* memory = malloc(memory_size);
  if (memory == NULL) {
    return 1;
  }
  memset(memory, 1, memory_size);
  const pid_t pgid = argc > 1 ? (pid_t)strtol(argv[1], NULL, 10) : 0;
  if (setpgid(0, pgid) != 0) {
    return 1;
  }
  for (;;) {
    pause();
  }
}

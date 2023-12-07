#include <stdio.h>

// Compile: gcc solution_A.c -o solution_A

int main(const int argc, const char** argv) {
  unsigned int house = 1;
  unsigned int elves[1000000];
  unsigned int i, sum, max;

  for (i = 0; i < 1000000; i++) {
    elves[i] = i;
  }

  while (house <= 1000000) {
    sum = 0;
    for (i = 0; i < house; i++) {
      elves[i]++;
      if (elves[i] == i + 1) {
        sum += (i + 1) * 10;
        elves[i] = 0;
      }
    }
    if (sum > max) max = sum;
    if (house % 10000 == 0) {
      printf("House %d got %d presents (%d).\n", house, sum, max);
    }
    if (sum >= 34000000) break;
    house++;
  }

  printf("%d\n", house);

  return 0;
}

#include <stdio.h>

// Compile: gcc solution_B.c -o solution_B

int main(const int argc, const char** argv) {
  unsigned int house = 1;
  unsigned int elves[2000000];
  unsigned int i, sum, max;

  for (i = 0; i < 1000000; i++) {
    elves[2*i] = i;
    elves[2*i+1] = 0;
  }

  while (house <= 1000000) {
    sum = 0;
    for (i = 0; i < house; i++) {
      elves[2*i]++;
      if (elves[2*i+1] < 50 && elves[2*i] == i + 1) {
        sum += (i + 1) * 11;
        elves[2*i] = 0;
        elves[2*i+1]++;
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

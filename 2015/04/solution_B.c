#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

// Compile: gcc solution_B.c -o md5 -lcrypto -lssl

int main(const int argc, const char** argv) {
  unsigned char input[30] = "yzbqklnj";
  unsigned char hash[MD5_DIGEST_LENGTH + 1];
  unsigned int i;

  for (i = 1; i <= 9999999; i++) {
    sprintf(input+8, "%d\0", i);
    MD5(input, strlen(input), hash);
    if (hash[0] == 0 && hash[1] == 0 && hash[2] == 0) {
      printf("%d\n", i);
      for (i = 0; i < 16; ++i) {
        printf("%02x", (unsigned int)hash[i]);
      }
      printf("\n");
      return 0;
    }
  }

  printf("FAIL\n");

  return 0;
}

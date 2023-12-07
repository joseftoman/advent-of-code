#!/usr/bin/perl
use warnings; use strict;
use Digest::MD5 'md5_hex';

my $input = <STDIN>;
chomp $input;
my $num = 1;

while (1) {
  if (substr(md5_hex($input, $num), 0, 5) eq '00000') {
    print "$num\n";
    last;
  }
  $num++;
}
